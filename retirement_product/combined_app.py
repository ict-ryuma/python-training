import streamlit as st
import pandas as pd
import joblib
import re

# モデル・エンコーダ読み込み
model = joblib.load("model.pkl")
le_job = joblib.load("le_job.pkl")
le_gender = joblib.load("le_gender.pkl")
le_divorce = joblib.load("le_divorce.pkl")

st.title("退職予測AI：フォーム + チャット 🎯")

# -------------------------------
# 🔹 フォーム入力エリア
# -------------------------------
with st.form("form_input"):
    st.subheader("📝 フォームで入力")
    age = st.number_input("年齢", min_value=18, max_value=70, value=30)
    job = st.selectbox("職業", ["営業", "Pythonエンジニア", "Goエンジニア", "デザイナー"])
    overtime = st.slider("残業時間", 0, 100, 20)
    gender = st.selectbox("性別", ["男性", "女性"])
    divorce = st.selectbox("離婚経験", ["なし", "あり"])
    power = st.slider("パワハラレベル", 0, 10, 3)
    submitted = st.form_submit_button("フォームで予測")

# 退職予測の結果表示（＋助言付き）
if submitted:
    df_base = {
        "年齢": age,
        "職業": le_job.transform([job])[0],
        "残業時間": overtime,
        "性別": le_gender.transform([gender])[0],
        "離婚": le_divorce.transform([divorce])[0],
    }

    # パワハラ感度の調整
    adjusted_power = int((10 - power) * 0.7)
    df = pd.DataFrame([{**df_base, "パワハラレベル": adjusted_power}])
    proba = model.predict_proba(df)[0][1]
    pred = model.predict(df)[0]

    if pred:
        st.error(f"😱 退職リスク高！（確率: {proba*100:.1f}％）")

        if proba > 0.6:
            best_level = power
            best_proba = proba
            for lvl in range(11):
                adjusted_lvl = int((10 - lvl) * 0.7)
                df_try = pd.DataFrame([{**df_base, "パワハラレベル": adjusted_lvl}])
                tmp_proba = model.predict_proba(df_try)[0][1]
                if tmp_proba < best_proba:
                    best_proba = tmp_proba
                    best_level = lvl

            if best_level != power:
                st.info(
                    f"💡 パワハラレベルを **{best_level}** にすると退職リスクが **{best_proba*100:.1f}%** まで下がります。\n"
                    f"職場の環境改善や相談の検討をおすすめします。"
                )
    else:
        st.success(f"💪 続けられる可能性高！（確率: {proba*100:.1f}％）")

# -------------------------------
# 🔹 チャット入力エリア
# -------------------------------
st.divider()
st.subheader("💬 チャットで入力")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# テキストから情報抽出
def extract_info(text):
    def find(pattern, default=None, cast=int):
        match = re.search(pattern, text)
        if match:
            return cast(match.group(1))
        return default

    age = find(r"年齢(\d+)")
    job = next((w for w in ["営業", "Pythonエンジニア", "Goエンジニア", "デザイナー"] if w in text), "営業")
    overtime = find(r"残業.*?(\d+)", default=0)
    gender = "男性" if "男性" in text else "女性"
    divorce = "あり" if re.search(r"離婚.*?(あり|して)", text) else "なし"
    power = find(r"パワハラ.*?(\d+)", default=0)

    return age, job, overtime, gender, divorce, power

# チャットからの診断処理
user_input = st.chat_input("あなたの状況を入力してね（例：年齢30歳、営業、残業80時間、男性、離婚なし、パワハラ7）")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    try:
        age, job, overtime, gender, divorce, power = extract_info(user_input)

        df = pd.DataFrame([{
            "年齢": age,
            "職業": le_job.transform([job])[0],
            "残業時間": overtime,
            "性別": le_gender.transform([gender])[0],
            "離婚": le_divorce.transform([divorce])[0],
            "パワハラレベル": int((10 - power) * 0.7)
        }])
        proba = model.predict_proba(df)[0][1]
        pred = model.predict(df)[0]

        result_msg = f"😱 退職の可能性が高いです（{proba*100:.1f}%）" if pred else f"💪 安心してください（{proba*100:.1f}%）"
    except Exception as e:
        result_msg = "⚠️ 入力内容がうまく読み取れませんでした。形式を見直してください。"

    st.session_state.messages.append({"role": "assistant", "content": result_msg})
    with st.chat_message("assistant"):
        st.write(result_msg)

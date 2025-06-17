import streamlit as st
import pandas as pd
import joblib
import os
from dotenv import load_dotenv
from openai import OpenAI

# 🔐 環境変数の読み込み
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 🎯 ページ設定
st.set_page_config(page_title="退職予測 & 相談チャット")
st.title("💼 退職リスク診断")

# ✅ モデルとエンコーダの読み込み
model = joblib.load("model.pkl")
le_job = joblib.load("le_job.pkl")
le_gender = joblib.load("le_gender.pkl")
le_divorce = joblib.load("le_divorce.pkl")

# 📝 退職予測フォーム
with st.form("input_form"):
    st.subheader("🧪 退職予測フォーム")
    age = st.number_input("年齢", 18, 70, 30)
    job = st.selectbox("職業", ["営業", "Pythonエンジニア", "Goエンジニア", "デザイナー"])
    overtime = st.slider("残業時間", 0, 100, 20)
    gender = st.selectbox("性別", ["男性", "女性"])
    divorce = st.selectbox("離婚経験", ["なし", "あり"])
    power = st.slider("パワハラレベル", 0, 10, 3)
    submitted = st.form_submit_button("退職確率をチェック！")

# 🎯 退職予測の結果表示（＋助言付き）
if submitted:
    df_base = {
        "年齢": age,
        "職業": le_job.transform([job])[0],
        "残業時間": overtime,
        "性別": le_gender.transform([gender])[0],
        "離婚": le_divorce.transform([divorce])[0],
    }

    df = pd.DataFrame([{**df_base, "パワハラレベル": power}])
    proba = model.predict_proba(df)[0][1]
    pred = model.predict(df)[0]

    if pred:
        st.error(f"😱 退職リスク高！（確率: {proba*100:.1f}％）")

        if proba > 0.6:
            # パワハラレベル調整でリスク低減を探る
            best_level = power
            best_proba = proba
            for lvl in range(11):
                df_try = pd.DataFrame([{**df_base, "パワハラレベル": lvl}])
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

# 💬 GPTチャット相談エリア
st.divider()
st.subheader("💁 カウンセラーに悩み相談")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_msg = st.chat_input("悩みを話してみてね（例：上司が怖くて出社したくない…）")

if user_msg:
    st.session_state.chat_history.append({"role": "user", "content": user_msg})
    with st.chat_message("user"):
        st.write(user_msg)

    with st.chat_message("assistant"):
        with st.spinner("カウンセラーが考え中..."):
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "あなたは優しく丁寧に人の心に寄り添うキャリアカウンセラーです。"},
                    {"role": "user", "content": user_msg}
                ]
            )
            assistant_msg = response.choices[0].message.content
            st.write(assistant_msg)
            st.session_state.chat_history.append({"role": "assistant", "content": assistant_msg})

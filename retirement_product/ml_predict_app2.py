import streamlit as st
import pandas as pd
import joblib

# タイトル表示
st.title("退職予測AIアプリ 🤖")
st.write("こんにちは！以下の情報を入力してください")

# 入力フォーム
age = st.number_input("年齢", min_value=18, max_value=70, value=30)
job = st.selectbox("職業", ["営業", "Pythonエンジニア", "Goエンジニア", "デザイナー"])
overtime = st.slider("残業時間", 0, 100, 20)
gender = st.selectbox("性別", ["男性", "女性"])
divorce = st.selectbox("離婚経験", ["なし", "あり"])
power_harassment = st.slider("パワハラレベル", 0, 10, 3)

# モデル・エンコーダ読み込み
model = joblib.load("model.pkl")
le_job = joblib.load("le_job.pkl")
le_gender = joblib.load("le_gender.pkl")
le_divorce = joblib.load("le_divorce.pkl")

# 予測ボタン
if st.button("AIに予測してもらう"):
    job_encoded = le_job.transform([job])[0]
    gender_encoded = le_gender.transform([gender])[0]
    divorce_encoded = le_divorce.transform([divorce])[0]

    # 入力データを DataFrame にまとめる
    new_data = pd.DataFrame([{
        "年齢": age,
        "職業": job_encoded,
        "残業時間": overtime,
        "性別": gender_encoded,
        "離婚": divorce_encoded,
        "パワハラレベル": power_harassment
    }])

    # モデル予測
    proba = model.predict_proba(new_data)[0][1]  # 退職する確率
    prediction = model.predict(new_data)[0]

    # 結果表示
    if prediction:
        st.error("退職する可能性が高いです 🥺")
    else:
        st.success("退職しない可能性が高いです 💪")

    # 退職確率を表示（%）
    st.metric("退職確率", f"{proba * 100:.1f} %")

    # 理由とTips表示
    reasons = []
    tips = []

    if overtime > 70:
        reasons.append("残業時間が非常に多いため")
        tips.append("業務量の調整や業務分担を検討しましょう。")

    if power_harassment >= 7:
        reasons.append("パワハラに耐えられなかったから。忍耐力なし！！")
        tips.append("もっと精神力が必要です。")

    if reasons:
        st.warning("⚠️ 退職リスクが高い理由: " + "、".join(reasons))
        st.info("💡 アドバイス: " + "／".join(tips))
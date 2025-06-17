import streamlit as st
import joblib
import pandas as pd
import re

model = joblib.load("model.pkl")  # ✅
le_job = joblib.load("le_job.pkl")
le_gender = joblib.load("le_gender.pkl")
le_divorce = joblib.load("le_divorce.pkl")

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
    divorce = "あり" if "離婚.*?あり" in text or "離婚して" in text else "なし"
    power = find(r"パワハラ.*?(\d+)", default=0)

    return age, job, overtime, gender, divorce, power

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("あなたの状況を入力してね（例：年齢30歳、営業、残業80時間、男性、離婚なし、パワハラ7）")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # 🔍 入力抽出
    age, job, overtime, gender, divorce, power = extract_info(user_input)

    input_df = pd.DataFrame([{
        "年齢": age,
        "職業": le_job.transform([job])[0],
        "残業時間": overtime,
        "性別": le_gender.transform([gender])[0],
        "離婚": le_divorce.transform([divorce])[0],
        "パワハラレベル": power
    }])

    proba = model.predict_proba(input_df)[0][1]
    prediction = model.predict(input_df)[0]

    if prediction:
        message = f"😱 退職の可能性が高いです（確率: {proba*100:.1f}%）"
    else:
        message = f"💪 安心してください。退職の可能性は低いです（確率: {proba*100:.1f}%）"

    st.session_state.messages.append({"role": "assistant", "content": message})
    with st.chat_message("assistant"):
        st.write(message)

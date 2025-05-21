import streamlit as st
import pandas as pd
import joblib

# タイトル表示（←これがないと真っ暗になります）
st.title("退職予測AIアプリ 🤖")
st.write("こんにちは！以下の情報を入力してください")

# 入力フォーム
age = st.number_input("年齢", min_value=18, max_value=70, value=30)
job = st.selectbox("職業", ["営業", "Pythonエンジニア", "Goエンジニア"])
overtime = st.slider("残業時間", 0, 100, 20)

# モデル読み込み
model = joblib.load("model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

# 予測処理（ボタンが押されたら）
if st.button("AIに予測してもらう"):
    job_encoded = label_encoder.transform([job])[0]
    new_data = pd.DataFrame([{
        "年齢": age,
        "職業": job_encoded,
        "残業時間": overtime
    }])
    
    prediction = model.predict(new_data)[0]
    
    if prediction:
        st.error("退職する可能性が高いです 🥺")
    else:
        st.success("退職しない可能性が高いです 💪")

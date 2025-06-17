# chatbot_retire_app.py
import streamlit as st
import pickle
import numpy as np

# モデルロード
with open("retire_predictor.pkl", "rb") as f:
    model = pickle.load(f)

st.title("💬 退職予測チャットボット")
st.write("あなたの状況を入力すると、退職確率をお伝えします。")

# 入力UI（簡易版）
age = st.number_input("あなたの年齢は？", min_value=18, max_value=65, step=1)
years = st.number_input("勤続年数は？", min_value=0, max_value=40, step=1)
overtime = st.number_input("月の残業時間は？", min_value=0, max_value=200, step=1)

if st.button("退職確率を診断する"):
    input_data = np.array([[age, years, overtime]])
    prob = model.predict_proba(input_data)[0][1]
    st.success(f"あなたの退職確率は **{prob*100:.1f}%** です。")

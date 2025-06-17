import streamlit as st
from survey_questions import questions
from survey_storage import save_response
from datetime import date

st.set_page_config(page_title="従業員サーベイ", layout="centered")
st.title("📋 月次パルスサーベイ")

st.markdown("**所要時間：3分** 率直にお答えください")

with st.form("survey_form"):
    response = {}
    for q in questions:
        if q["type"] == "slider":
            response[q["key"]] = st.slider(q["label"], 0, 10, 5)
        elif q["type"] == "text":
            response[q["key"]] = st.text_area(q["label"])

    submitted = st.form_submit_button("送信する")

if submitted:
    save_response(response)
    st.success("✅ 回答を受け付けました！ありがとうございました！")

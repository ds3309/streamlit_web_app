import streamlit as st

with st.form(key = "profile_form"):
    name = st.text_input("名前")
    address = st.text_input("住所")

    # age_category = st.selectbox(
    age_category = st.radio(
        "年齢層",
        ("子供", "大人")
    )
    
    hobby = st.multiselect(
        "趣味",
        ("スポーツ", "読書", "映画")
    )
    
    submit_btn = st.form_submit_button("送信")
    cancel_btn = st.form_submit_button("キャンセル")

if submit_btn:
    st.text(f"ようこそ！{name}さん、{address}に書類を送りました")
    st.text(f"年齢層：{age_category}")
    st.text(f"趣味：{','.join(hobby)}")
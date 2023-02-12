import streamlit as st

code = """
import streamlit as st

st.title("テストアプリ")
"""
st.code(code, language="python")
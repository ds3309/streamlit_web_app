import streamlit as st
from PIL import Image #画像読み込み用ライブラリ

st.title("テストアプリ")
st.caption("これはテストアプリです")

image = Image.open("./data/1655111961240.png")
st.image(image, width=200)
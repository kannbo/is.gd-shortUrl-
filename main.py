import streamlit as st,uuid,os
import requests as req
st.header("shorking url")
st.write("このアプリはis.gdを用いてショートURLを生成します")
url=st.text_input("URL")
if st.button("作成"):
  try:
    _url=request.get(f"https://is.gd/create.php?format=simple&url={url}").text
    st.write(f"生成完了!:{_url}")
  except Exception as e:
    st.write("<style>red:{  color:red;}</style><red>生成失敗!:"+str(e)+"</red>",unsafe_allow_html=True)

import streamlit as st

st.title("Power BI 簡報說明")

tab1, tab2, tab3 = st.tabs(["韓國", "日本", "加拿大"])

with tab1:
    st.header("韓國")
    st.image("img/tab1.jpg", caption="韓國旅遊")

with tab2:
    st.header("日本")
    st.image("img/tab2.jpg", caption="日本旅遊")

with tab3:
    st.header("加拿大")
    st.image("img/tab3.jpg", caption="加拿大旅遊")
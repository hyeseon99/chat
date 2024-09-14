import streamlit as st

# 첫 페이지: 음식점 / 병원 선택
st.title("서비스 선택")

col1, col2 = st.columns(2)

with col1:
    if st.button("음식점"):
        st.write("음식점 페이지로 이동")
        # 음식점 페이지로 이동 코드
        # 음식을 선택하고, 메뉴, 가격 등을 표시하는 코드 추가 가능

with col2:
    if st.button("병원"):
        st.write("챗봇 페이지로 이동")
        # 병원 페이지로 이동 코드
        # 챗봇 인터페이스 및 API 연동 구현

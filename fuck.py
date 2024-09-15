import streamlit as st

# 상단 바
st.title("세종시를 '세먹자!'")
st.caption("성별을 선택해 주세요:")
gender = st.radio("성별:", ('여자', '남자'))


st.caption("연령대를 선택해 주세요:")
age_group = st.selectbox("연령대:", ['10대', '20대', '30대', '40대','50대','60대','70대 이상'])

st.caption("음식 카테고리를 골라주세요:")
region = st.selectbox("음식 카테고리:", ['한식', '중식', '일식', '양식', '아시안', '분식', '카페','간식','제과점','주점업','패스트푸드','치킨전문점'])

# 메인 컨텐츠 영역
st.header("가게 옵션")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("가게 이름")
    st.image("https://via.placeholder.com/150", caption="가게 이미지")
    st.text("메뉴: 가게메뉴")
    st.text("가격: 가격")
    st.text("평점: 평점")

with col2:
    st.subheader("가게 이름")
    st.image("https://via.placeholder.com/150", caption="가게 이미지")
    st.text("메뉴: 가게메뉴")
    st.text("가격: 가격")
    st.text("평점: 평점")

with col3:
    st.subheader("가게 이름")
    st.image("https://via.placeholder.com/150", caption="가게 이미지")
    st.text("메뉴: 가게메뉴")
    st.text("가격: 가격")
    st.text("평점: 평점")

with col4:
    st.subheader("가게 이름")
    st.image("https://via.placeholder.com/150", caption="가게 이미지")
    st.text("메뉴: 가게메뉴")
    st.text("가격: 가격")
    st.text("평점: 평점")

pip install streamlit-toggle-switch
import streamlit as st
import streamlit_toggle as tog

# 상단 바
st.title("세시를 '세먹자!'")
st.caption("성별을 선택해 주세요:")

# 토글 스위치로 성별 선택 구현
gender_toggle = tog.st_toggle_switch(label="여자", 
                                     key="gender_toggle", 
                                     default_value=True,  # 기본값을 True로 설정 (여자 선택)
                                     label_after=False, 
                                     inactive_color='#D3D3D3', 
                                     active_color="#11567f", 
                                     track_color="#29B5E8")

# 성별 값을 설정 (토글 값에 따라 여자 또는 남자)
gender = "여자" if gender_toggle else "남자"
st.write(f"선택된 성별: {gender}")

st.caption("연령대를 선택해 주세요:")
age_group = st.selectbox("연령대:", ['10대', '20대', '30대', '40대', '50대', '60대', '70대 이상'])

st.caption("음식 카테고리를 골라주세요:")
region = st.selectbox("음식 카테고리:", ['한식', '중식', '일식', '양식', '아시안', '분식', '카페', '간식', '제과점', '주점업', '패스트푸드', '치킨전문점'])

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

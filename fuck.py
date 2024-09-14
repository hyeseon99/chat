import streamlit as st

# 첫 화면 설정
if 'page' not in st.session_state:
    st.session_state.page = "main"

def go_to_restaurant():
    st.session_state.page = "restaurant"

def go_to_hospital():
    st.session_state.page = "hospital"

# CSS 적용
st.markdown("""
    <style>
    .container {
        display: flex;
        height: 100vh;
    }
    .left {
        background-color: #FDEADE;
        width: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .right {
        background-color: #D6EAF8;
        width: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .button {
        font-size: 24px;
        font-weight: bold;
        padding: 10px;
        width: 200px;
        margin: 10px;
        text-align: center;
        border-radius: 10px;
        border: 2px solid #ddd;
        cursor: pointer;
    }
    </style>
    """, unsafe_allow_html=True)

# 페이지 상태에 따라 다른 화면 렌더링
if st.session_state.page == "main":
    st.title("서비스 선택")

    st.markdown('<div class="container">', unsafe_allow_html=True)

    # 왼쪽 (음식점)
    st.markdown('<div class="left">', unsafe_allow_html=True)
    if st.button("음식점 선택"):
        go_to_restaurant()
    st.markdown('</div>', unsafe_allow_html=True)

    # 오른쪽 (병원)
    st.markdown('<div class="right">', unsafe_allow_html=True)
    if st.button("병원 선택"):
        go_to_hospital()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "restaurant":
    st.title("음식점 페이지")
    st.write("여기에서 음식점을 추천합니다.")
    if st.button("뒤로 가기"):
        st.session_state.page = "main"

elif st.session_state.page == "hospital":
    st.title("병원 페이지")
    st.write("병원 관련 서비스를 제공합니다.")
    if st.button("뒤로 가기"):
        st.session_state.page = "main"

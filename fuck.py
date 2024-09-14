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
        justify-content: center;
        align-items: center;
        height: 100vh;
    }
    .box {
        margin: 0 20px;
        text-align: center;
    }
    img {
        width: 250px;
        height: 250px;
        margin-bottom: 10px;
    }
    .button {
        font-size: 20px;
        font-weight: bold;
        padding: 10px;
        width: 150px;
        margin: 10px auto;
        text-align: center;
        border-radius: 10px;
        border: 2px solid #ddd;
    }
    </style>
    """, unsafe_allow_html=True)

# 페이지 상태에 따라 다른 화면 렌더링
if st.session_state.page == "main":
    st.title("서비스 선택")
    
    st.markdown('<div class="container">', unsafe_allow_html=True)
    
    # 음식점 이미지 및 버튼
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.image("https://raw.githubusercontent.com/hyeseon99/chat/main/음식.PNG")
    if st.button("음식점"):
        go_to_restaurant()
    st.markdown('<div class="button">음식점</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 병원 이미지 및 버튼
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.image("https://raw.githubusercontent.com/hyeseon99/chat/main/병원.PNG")
    if st.button("병원"):
        go_to_hospital()
    st.markdown('<div class="button">병원</div>', unsafe_allow_html=True)
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

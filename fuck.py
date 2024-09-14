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
        justify-content: space-around;
        align-items: center;
        height: 100vh;
    }
    .box {
        width: 400px;
        height: 500px;
        border-radius: 20px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        margin: 0 20px;
    }
    .restaurant {
        background-color: #FDEADE;
    }
    .hospital {
        background-color: #D6EAF8;
    }
    img {
        width: 200px;
        height: 200px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .button {
        font-size: 24px;
        font-weight: bold;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# 페이지 상태에 따라 다른 화면 렌더링
if st.session_state.page == "main":
    st.title("서비스 선택")
    
    st.markdown('<div class="container">', unsafe_allow_html=True)
    
    # 음식점 부분
    st.markdown('<div class="box restaurant">', unsafe_allow_html=True)
    st.image("https://raw.githubusercontent.com/hyeseon99/chat/main/음식.PNG")  # 음식점 이미지 경로
    if st.button("음식점"):
        go_to_restaurant()
    st.markdown('<div class="button">음식점</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 병원 부분
    st.markdown('<div class="box hospital">', unsafe_allow_html=True)
    st.image("https://raw.githubusercontent.com/hyeseon99/chat/main/병원.PNG")  # 병원 이미지 경로
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

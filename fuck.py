import streamlit as st

# 첫 화면
if 'page' not in st.session_state:
    st.session_state.page = "main"

def go_to_restaurant():
    st.session_state.page = "restaurant"

def go_to_hospital():
    st.session_state.page = "hospital"

# 페이지 상태에 따라 다른 페이지 렌더링
if st.session_state.page == "main":
    st.title("서비스 선택")

    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("음식점"):
            go_to_restaurant()
    
    with col2:
        if st.button("병원"):
            go_to_hospital()

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

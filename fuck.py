import streamlit as st

# CSS 적용
st.markdown("""
    <style>
    .container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 80vh;
    }
    .box {
        width: 300px;
        height: 400px;
        border-radius: 20px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        margin: 0 20px;
    }
    .restaurant {
        background-color: #FDEADE;
    }
    .hospital {
        background-color: #D6EAF8;
    }
    img {
        width: 150px;
        height: 150px;
    }
    .button {
        margin-top: 20px;
        font-size: 20px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="container">', unsafe_allow_html=True)

# 음식점 부분
st.markdown('<div class="box restaurant">', unsafe_allow_html=True)
st.image('음식점_이미지.png')  # 음식점 이미지를 여기에 추가
st.markdown('<div class="button">음식점</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 병원 부분
st.markdown('<div class="box hospital">', unsafe_allow_html=True)
st.image('병원_이미지.png')  # 병원 이미지를 여기에 추가
st.markdown('<div class="button">병원</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

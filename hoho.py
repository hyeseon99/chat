pip install streamlit-toggle-switch

import streamlit as st
import urllib3
import json

# ETRI API 설정
openApiURL = "http://aiopen.etri.re.kr:8000/WiseQAnal"
accessKey = "074c136c-f5d7-4063-811b-9cf8b8060803"  # 본인의 API 키로 변경하세요.

# 병원 관련 질문-답변 세트
hospital_questions = {
    "진료 시간": "병원의 진료 시간은 오전 9시부터 오후 6시까지입니다.",
    "응급실 위치": "응급실은 본관 1층에 위치하고 있습니다.",
    "의사 정보": "내과의 김철수 의사, 소아과의 박영희 의사가 있습니다.",
    "예약 방법": "진료 예약은 병원 홈페이지나 전화로 가능합니다."
}

# ETRI API 호출 함수
def get_response(question):
    requestJson = {
        "access_key": accessKey,
        "argument": {
            "text": question,
            "analysis_code": "QA"
        }
    }

    http = urllib3.PoolManager()
    response = http.request(
        "POST",
        openApiURL,
        headers={"Content-Type": "application/json; charset=UTF-8"},
        body=json.dumps(requestJson)
    )
    return json.loads(response.data.decode('utf-8'))

# 질문 전처리 함수
def preprocess_question(question):
    return question.replace(" ", "").strip().lower()

# Streamlit 레이아웃 구성
st.set_page_config(page_title="병원 상담 챗봇", layout="wide")

# 배경 이미지 스타일
st.markdown(
    """
    <style>
    .main {
        background-image: url("https://raw.githubusercontent.com/hyeseon99/chat/main/hohoho.jpg");
        background-size: cover;
        background-position: center;
        height: 100vh;
    }
    .chat-box {
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 350px;
        padding: 20px;
        background-color: #f9f9f9;
        border-radius: 10px;
        box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1);
        z-index: 1000;
    }
    .chat-header {
        background-color: #1a73e8;
        color: white;
        padding: 10px;
        border-radius: 10px 10px 0 0;
        text-align: center;
        font-weight: bold;
    }
    .chat-footer {
        background-color: #f1f1f1;
        padding: 10px;
        border-radius: 0 0 10px 10px;
        text-align: center;
    }
    .send-btn {
        margin-top: 10px;
        width: 100%;
        padding: 10px;
        background-color: #34a853;
        color: white;
        border: none;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True
)

# 배경 화면 설정
st.markdown('<div class="main">', unsafe_allow_html=True)

# 오른쪽 하단에 고정된 챗봇 UI
st.markdown("""
    <div class="chat-box">
        <div class="chat-header">병원 상담 챗봇</div>
        <div class="chat-footer">
            <input type="text" id="chatInput" style="width: 100%; padding: 8px; border-radius: 5px; border: 1px solid #ccc;" placeholder="질문을 입력하세요">
            <button class="send-btn" onclick="send_message()">전송</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 사용자 입력과 챗봇 응답 처리
user_question = st.text_input("질문을 입력하세요:", key="user_input")

if st.button("전송", key="send_button"):
    user_question = preprocess_question(user_question)
    
    if user_question:
        st.write(f"사용자: {user_question}")
        
        # 키워드 기반 매칭
        if "진료" in user_question and "시간" in user_question:
            st.write(f"챗봇: {hospital_questions['진료 시간']}")
        elif "응급실" in user_question and "위치" in user_question:
            st.write(f"챗봇: {hospital_questions['응급실 위치']}")
        elif "의사" in user_question and "정보" in user_question:
            st.write(f"챗봇: {hospital_questions['의사 정보']}")
        elif "예약" in user_question:
            st.write(f"챗봇: {hospital_questions['예약 방법']}")
        else:
            # API 호출로 응답 가져오기
            result = get_response(user_question)
            answer = result.get('return_object', {}).get('answer', '관련 정보를 찾을 수 없습니다.')
            st.write(f"챗봇: {answer}")

st.markdown('</div>', unsafe_allow_html=True)

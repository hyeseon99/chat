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
    "의사 정보": "내과의 김철수 의사, 소아과의 박영희 의사가 있습니다."
}

# ETRI API 응답 함수
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

# Streamlit UI 구성
st.title("병원 상담 챗봇")
st.write("ETRI WiseQAnal API를 사용한 병원 관련 질문 분석")

# 사용자 입력
user_question = st.text_input("질문을 입력하세요:")

if st.button("전송"):
    user_question = preprocess_question(user_question)
    
    if user_question:
        st.write(f"사용자: {user_question}")
        
        # 키워드 기반 매칭
        if "진료" in user_question and "시간" in user_question:
            st.write("챗봇: 병원의 진료 시간은 오전 9시부터 오후 6시까지입니다.")
        elif "응급실" in user_question and "위치" in user_question:
            st.write("챗봇: 응급실은 본관 1층에 위치하고 있습니다.")
        elif "진료" in user_question:
            st.write("챗봇: 병원의 진료는 예약제로 운영됩니다. 자세한 정보는 병원 홈페이지를 참고해 주세요.")
        elif "시간" in user_question:
            st.write("챗봇: 병원의 운영 시간은 오전 9시부터 오후 6시까지입니다.")
        elif "위치" in user_question:
            st.write("챗봇: 병원은 서울시 강남구에 위치해 있습니다.")
        else:
            result = get_response(user_question)
            answer = result.get('return_object', {}).get('answer', '관련 정보를 찾을 수 없습니다.')
            st.write(f"챗봇: {answer}")

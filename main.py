import streamlit as st
import openai

# OpenAI API 키를 st.secrets에서 읽어옴
openai.api_key = st.secrets["OPENAI_API_KEY"]

# 기본 설정
st.set_page_config(page_title="시설물 관리 시스템", page_icon="🏢", layout="wide")

# 웹앱 제목
st.title("시설물 관리 시스템")
st.write("시설물 관리와 관련된 질문을 하세요. OpenAI 모델이 도와드립니다.")

# 사용자 입력 받기
user_input = st.text_input("시설물 관련 질문을 입력하세요:")

# OpenAI API를 사용하여 답변 생성
if user_input:
    try:
        # 최신 OpenAI API 방식에 맞춰서 대화형 모델 호출
        response = openai.chat_completions.create(
            model="gpt-3.5-turbo",  # gpt-3.5-turbo 모델 사용
            messages=[{"role": "user", "content": user_input}],
        )
        
        # 생성된 답변을 화면에 출력
        answer = response['choices'][0]['message']['content']
        st.write("**답변:**", answer)
    except Exception as e:
        st.error(f"오류가 발생했습니다: {e}")

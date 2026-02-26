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
        # OpenAI의 GPT 모델을 통해 답변 생성
        response = openai.Completion.create(
            engine="text-davinci-003",  # 최신 모델을 사용
            prompt=user_input,
            max_tokens=150,
            temperature=0.7
        )
        # 생성된 답변을 화면에 출력
        answer = response.choices[0].text.strip()
        st.write("**답변:**", answer)
    except Exception as e:
        st.error(f"오류가 발생했습니다: {e}")

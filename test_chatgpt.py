import openai
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# 환경 변수에서 API 키 가져오기
api_key = os.getenv('OPENAI_API_KEY')

# OpenAI API 키 설정
openai.api_key = api_key

text_input = "인공지능에 대해 알려줘"

# OpenAI API 호출
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": text_input}
    ]
)

# 응답 출력
print(completion.choices[0].message['content'])

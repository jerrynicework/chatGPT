import openai
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# 환경 변수에서 API 키 가져오기
api_key = os.getenv('OPENAI_API_KEY')

# OpenAI API 키 설정
openai.api_key = api_key

# OpenAI API 호출
try:
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # 모델 이름을 gpt-3.5-turbo로 설정
        messages=[
            {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
            {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
        ]
    )

    # 응답 출력
    print(completion.choices[0].message['content'])
except openai.error.RateLimitError as e:
    print("Rate limit exceeded. Please check your plan and billing details.")
except openai.error.OpenAIError as e:
    print(f"An error occurred: {e}")

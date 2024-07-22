import openai
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# 환경 변수에서 API 키 가져오기
api_key = os.getenv('OPENAI_API_KEY')

# OpenAI API 키 설정
openai.api_key = api_key

audio_file = open("audio_input.wav", "rb")
transcription = openai.Audio.transcribe(
    model="whisper-1", 
    file=audio_file
)
print(transcription['text'])

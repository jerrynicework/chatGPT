import openai
import os
from dotenv import load_dotenv
from gtts import gTTS
from pathlib import Path
# .env 파일 로드
load_dotenv()
# 환경 변수에서 API 키 가져오기
api_key = os.getenv('OPENAI_API_KEY')
# OpenAI API 키 설정
openai.api_key = api_key
####################################
########## 함수 구조 만들기 ############
####################################
def conn_whisper() :
    return text_input

def conn_chatgpt(text_input) :
    return text_output

def conn_tts(text_output) :
    return audio_output_path

def main() :
    # 마이크 input => audio_input_path
    text_input = conn_whisper()
    text_output = conn_chatgpt(text_input)
    audio_output_path = conn_tts(text_output)
    # audio_output_path의 mp3를 play
    return 

main()

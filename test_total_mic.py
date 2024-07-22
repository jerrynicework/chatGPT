import openai
import os
from dotenv import load_dotenv
from gtts import gTTS
from pathlib import Path
import sounddevice as sd
from scipy.io.wavfile import write
from playsound import playsound


# .env 파일 로드
load_dotenv()
# 환경 변수에서 API 키 가져오기
api_key = os.getenv('OPENAI_API_KEY')
# OpenAI API 키 설정
openai.api_key = api_key
####################################
########## 함수 구조 만들기 ############
####################################


def record_audio() :
    
    # 비트레이트
    fs = 44100
    seconds = 3
    
    print('녹음을 시작합니다.')
    record = sd.rec(int(seconds*fs), samplerate=fs, channels=1)
    sd.wait()
    print('녹음을 종료합니다.')
    
    
    audio_input_path = "audio_input.wav"
    write(audio_input_path, fs, record)
    
    return audio_input_path

def conn_whisper(audio_input_path) :
    audio_file = open(audio_input_path, "rb")
    
    transcription = openai.Audio.transcribe(
        model="whisper-1", 
        file=audio_file
    )
    print(transcription['text'])
    text_input = transcription['text']
    return text_input

def conn_chatgpt(text_input) :
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": text_input}
        ]
    )
    print(completion.choices[0].message['content'])
    text_output = completion.choices[0].message['content']
    return text_output

def conn_tts(text_output) :
    # gTTS 객체 생성
    tts = gTTS(text=text_output, lang='ko')
    # 파일 저장 경로 설정
    speech_file_path = Path(__file__).parent / "audio_output.mp3"
    # 파일로 저장
    tts.save(speech_file_path)
    print(f"Audio saved to {speech_file_path}")
    audio_output_path = str(speech_file_path)
    return audio_output_path

def main() :
    # 마이크 input => audio_input_path
    audio_input_path = record_audio()
    text_input = conn_whisper(audio_input_path)
    text_output = conn_chatgpt(text_input)
    audio_output_path = conn_tts(text_output)
    playsound(audio_output_path)
    # audio_output_path의 mp3를 play
    return 

main()

from gtts import gTTS
from pathlib import Path

# 텍스트 입력
text_input = "Today is a wonderful day to build something people love!"

# gTTS 객체 생성
tts = gTTS(text=text_input, lang='en')

# 파일 저장 경로 설정
speech_file_path = Path(__file__).parent / "audio_output.mp3"

# 파일로 저장
tts.save(speech_file_path)

print(f"Audio saved to {speech_file_path}")

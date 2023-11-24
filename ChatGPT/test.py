import openai
import json

# 현재 폴더 경로 확인
# import os
# print(os.getcwd())

"""
# 테스트 성공
# 음성 -> 문자 테스트
openai.api_key = "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"

# 음성 -> 문자
# 서울의 중심에는 한강 하류가 동에서 서쪽으로 흐르고 있다.
audio_file = open("./test.m4a", "rb")

# audio -> text
transcript = openai.Audio.transcribe(model="whisper-1", file=audio_file)
# json으로 받아올 때 아스키 값으로 변환되서 UTF-8로 인코딩 하는 옵션을 추가
ts2str = json.dumps(transcript, ensure_ascii=False)

print(ts2str)

"""
###########################################################################
"""
# chat-gpt api 기본 사용법 ()

openai.api_key = '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'
# 키 만들때 1번만 보여주니 잃어버리면 재생성 필요함.

messages = []
while True:
    content = input("User: ")
    messages.append({"role":"user", "content":content})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=messages
    )

    chat_response = completion.choices[0].message.content
    print(f'ChatGPT: {chat_response}')
    messages.append({"role":"assistant", "content":chat_response})

"""
###########################################################################
"""
#audio test

import openai


audio_file = open("/path/to/file/audio.mp3", "rb")
# audio -> text
transcript = openai.Audio.transcribe("whisper-1", audio_file)
# language translate
transcript = openai.Audio.translate("whisper-1", audio_file)
"""

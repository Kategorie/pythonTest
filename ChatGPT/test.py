import openai

# import os

# print(os.getcwd())

# 음성 -> 문자 테스트
openai.api_key = "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"
api_key = "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"
# 음성 -> 문자
audio_file = open("./test.m4a", "rb")

# audio -> text
transcript = openai.Audio.transcribe("whisper-1", audio_file, api_key)

print(transcript)

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

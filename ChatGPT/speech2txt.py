########################################################################
# 1. 오디오 -> 텍스트 변환 함수 : speech2Text
########################################################################
import openai  # chat-gpt
import json  # S to T json utf 변환

# using whisper-1 model
# 오디오 입력 관련해서 클래스 수정 필요


class speech2Text:
    # 키 만들때 1번만 보여주니 잃어버리면 재생성 필요함.
    openai.api_key = "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"

    def s2T(self, audio):  # return str
        # 음성 -> 문자
        # 서울의 중심에는 한강 하류가 동에서 서쪽으로 흐르고 있다.
        audio_file = open("./test.m4a", "rb")

        # audio -> text
        transcript = openai.Audio.transcribe(model="whisper-1", file=audio_file)
        # json으로 받아올 때 아스키 값으로 변환되서 UTF-8로 인코딩 하는 옵션을 추가
        ts2str = json.dumps(transcript, ensure_ascii=False)

        return ts2str
        # print(ts2str)

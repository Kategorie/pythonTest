import openai  # chat-gpt
import os  # 폴더 및 파일 접근
import fnmatch  # 파일에 대한 작업
import shutil  # 파일 복사
import json  # S to T json utf 변환

"""
# 키 만들때 1번만 보여주니 잃어버리면 재생성 필요함.
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


# 문자 -> 단어 추출 (문장에서 단어 추출하는 법, 또는 검색하는 알고리즘)
# 특정 단어에 대해서 해당 기능 호출
# 폴더 열기
class openFolder:
    classCount = 0
    folder_list = ""  # 클래스 변수(클래스 생성시 고정값)

    def __init__(self):  # -> 는 리턴값이 어떤지 명시해주기 위해서 사용한다.
        print("create openFolder")
        openFolder.classCount += 1
        print(openFolder.classCount)  # 클래스 변수 접근 방법

    def init_root_path(self, text_path):
        self.root_path = text_path
        print(self.root_path)  # 인스턴스 변수(각 클래스에 별개로 저장되는 값)
        print("check root_path")

    def init_folder_list(self):
        self.folder_list = [
            name
            for name in os.listdir(self.root_path)
            if os.path.isdir(os.path.join(self.root_path, name))
        ]
        print(self.folder_list)
        print("check folder_list")

    def create_folder(self):
        for folder in self.folder_list:
            try:
                if not os.path.exists(self.root_path + folder + "\\새폴더명1\\"):
                    os.makedirs(self.root_path + folder + "\\새폴더명1\\")
            except OSError:
                print(
                    "Error: " + self.root_path + folder + "\\새폴더명1\\" + "폴더 생성에 실패했습니다."
                )

            try:
                if not os.path.exists(self.root_path + folder + "\\새폴더명2\\"):
                    os.makedirs(self.root_path + folder + "\\새폴더명2\\")
            except OSError:
                print(
                    "Error: " + self.root_path + folder + "\\새폴더명2\\" + "폴더 생성에 실패했습니다."
                )


# 파일 실행
class openFile:
    # 이 클래스는 openFolder 클래스의 하위 클래스로 openFolder에서 file 작업을 모두 처리하도록 작업.
    def __init__(self):
        # 파일 실행
        os.startfile("c:\\폴더명\\파일명.xlsx")
        print("create openFile")

    def open_file():
        for file in os.listdir("c:\\폴더명\\"):
            # 해당 파일이 엑셀 파일이면 수행할 작업
            if fnmatch.fnmatch(file, "*.xlsx"):
                pass
            # 해당 파일이 csv 파일이면 수행할 작업
            elif fnmatch.fnmatch(file, "*.csv"):
                pass

    def copy_file():
        file_from = "c:\\폴더명\\파일명.xlsx"
        file_to = "c:\\폴더명\\파일명.xlsx"
        shutil.copy(file_from, file_to)

    def delete_file():
        os.remove("c:\\폴더명\\파일명.xlsx")


# 크롬 열기
# 크롬 열고 검색하기

# 메인
if __name__ == "__main__":
    aa = openFolder()
    aa.init_root_path("D:\Download\Garage\Garage")
    aa.init_folder_list()

import os  # 폴더 및 파일 접근
import fnmatch  # 파일에 대한 작업
import shutil  # 파일 복사

####################################################################
# 작성 함수 리스트
from fileFunction import *
from folderFunction import *

####################################################################
# 문자 -> 단어 추출 (문장에서 단어 추출하는 법, 또는 검색하는 알고리즘)
# 특정 단어에 대해서 해당 기능 호출


# 파일 실행
class openFile:
    # 이 클래스는 openFolder 클래스의 하위 클래스로 openFolder에서 file 작업을 모두 처리하도록 작업.
    def __init__(self):
        # 파일 실행
        os.startfile("c:\\폴더명\\파일명.xlsx")
        print("create openFile")

    def open_file(self):
        for file in os.listdir("c:\\폴더명\\"):
            # 해당 파일이 엑셀 파일이면 수행할 작업
            if fnmatch.fnmatch(file, "*.xlsx"):
                pass
            # 해당 파일이 csv 파일이면 수행할 작업
            elif fnmatch.fnmatch(file, "*.csv"):
                pass

    def copy_file(self):
        file_from = "c:\\폴더명\\파일명.xlsx"
        file_to = "c:\\폴더명\\파일명.xlsx"
        shutil.copy(file_from, file_to)

    def delete_file(self):
        os.remove("c:\\폴더명\\파일명.xlsx")


# 루트 경로 받아와서 파일이나 폴더 탐색
class findFileWithFolder:
    file_list = []

    def __init__(self):
        pass

    # 찾고자 하는 경로에서 하위로 찾을 파일 및 폴더 이름 검색
    def find_file(self, root_path, find_name):
        print("파일 탐색")
        # 현재 보고 있는 폴더 이름, parent 폴더 내 폴더 리스트, parent 폴더 내 파일 리스트
        for parent, _, files in os.walk(root_path):
            for f in files:
                if f == find_name:
                    self.file_list.append(f)

        print(self.file_list)


# 크롬 열기
# 크롬 열고 검색하기

# 메인
if __name__ == "__main__":
    folder_test = openFolder()
    folder_name = "hello"

    folder_test.init_root_path("D:/Download/Garage/Garage")
    folder_test.init_folder_list()
    folder_test.init_file_list()
    folder_test.create_folder(folder_name)

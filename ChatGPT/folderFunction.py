import os  # 폴더 및 파일 접근


# 루트 경로 받아와서 폴더 열기
class openFolder:
    classCount = 0
    root_path = ""
    folder_list = []  # 클래스 변수(클래스 생성시 고정값)
    file_list = []

    def __init__(self):  # -> 는 리턴값이 어떤지 명시해주기 위해서 사용한다.
        print("create openFolder")
        openFolder.classCount += 1
        print(openFolder.classCount)  # 클래스 변수 접근 방법

    # 루트 경로 설정
    def init_root_path(self, root_path):
        print("check root_path")
        self.root_path = root_path
        print(self.root_path)  # 인스턴스 변수(각 클래스에 별개로 저장되는 값)

    # 폴더 목록 반환
    def init_folder_list(self):
        print("check folder_list")
        self.folder_list = [
            name
            for name in os.listdir(self.root_path)
            if os.path.isdir(os.path.join(self.root_path, name))
        ]
        print(self.folder_list)

    # 파일 목록 반환
    def init_file_list(self):
        print("check file_list")
        self.file_list = [
            name for name in os.listdir(self.root_path) if name.count(".")
        ]
        print(self.file_list)


class creathFolder:
    root_path = ""

    def __init__(self):
        pass

    # 폴더 생성
    def create_folder(self, folder_name):
        # for folder in self.folder_list:
        try:
            if not os.path.exists(self.root_path + "\\" + folder_name + "\\"):
                os.makedirs(self.root_path + "\\" + folder_name + "\\")
                print(folder_name, "폴더를 생성했습니다.")
        except OSError:
            print(
                "Error: "
                + self.root_path
                + "\\"
                + folder_name
                + "\\"
                + "폴더 생성에 실패했습니다."
            )

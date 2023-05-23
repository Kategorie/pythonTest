# init 에서 패키지 import 하고자하는 모듈 설정
# __all__ : 현재 패키지 디렉터리에서 * 기호를 사용하여 import할 경우 
# 이곳에 정의된 echo 모듈만 import된다는 의미이다.
# __all__ = ['echo']

LASTUPDATE="5/22/23"

def print_lastUpdate_info() :
    print("the last update date is {LASTUPDATE}")

# 여기에 패키지 초기화 코드 작성
print("Initializing ...")
"""
# 포매팅 정렬 방법
# : 이거 앞에는 매개변수 순서를 나타냄
# 실수는 : 이거 뒤에 "앞자리.뒷자리f" 형태로 씀
# 이와 같이 문자열은 s, 실수는 f 등으로 뒤에 붙음
S = {"a": "11", "b": "2222222222", "c": "3223"}, {
    "a": "111111111",
    "b": "2222",
    "c": "3223",
}

for i in range(len(S)):
    print("{:<15}{:<15}{:<15}".format(S[i]["a"], S[i]["b"], S[i]["c"]))
"""

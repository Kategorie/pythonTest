print()
pass
####################################################################### readline 사용법
# map 사용 시
import sys

a, b, c = map(int, sys.stdin.readline().split())
# 반복 문자열 입력 시
for i in range(10):
    a = sys.stdin.readline().rstrip()

####################################################################### dict 사용법
# 응용
before = ["a", "b", "c", "d"]
after = ["aa", "bb", "cc", "dd"]

# 사전 만들기
temp_dict = {}
for i, j in zip(before, after):
    temp_dict[i] = j

# 매핑할 list
mapping_list = ["b", "c", "b", "b", "a"]

# list comprehension 사용
mapping_list_ = [temp_dict[k] for k in before]
print(mapping_list_)
####################################################################### 테스트 용 랜덤 인풋 생성
# 랜덤값 생성
import random

test_num = 500000
test_start = -10000000
test_end = 10000000 + 1
test_list_1 = []
test_list_2 = []
for test in range(test_num):
    test_list_1.append(random.randrange(test_start, test_end))
    test_list_2.append(random.randrange(test_start, test_end))
####################################################################### 시간 측정 코드
# 시간측정 함수
import time

time_start = time.time()

time_end = time.time()
time_result = time_end - time_start
print(str(time_result))
####################################################################### 이건 뭐지;;
N = int(input())
A = []
A = list(map(int, input().split()))

M = int(input())
B = []
B = list(map(int, input().split()))

res = []
for i in B:
    if A.count(i):
        res.append(1)
    else:
        res.append(0)

for j in res:
    print(j, end=" ")
"""
N = int(input())
A = []
for _1 in range(N):
    A.append(map(int, input().split()))

M = int(input())
B = []
for _2 in range(M):
    B.append(map(int, input().split()))

res = []
for i in B:
    if A.count(i):
        res.append(1)
    else:
        res.append(0)

for _3 in res:
    print(_3, end=" ")
# 문제가 서로 섞인 느낌... 이 코드 다른 문제에서 쓸 수 있을듯
N = 5  # int(input())
A = [6, 3, 2, 10, -10]
# for _1 in range(N):
#    A.append(map(int, input().split()))

M = 8  # int(input())
B = [10, 9, -5, 2, 3, 4, 5, -10]
# for _2 in range(M):
#    B.append(map(int, input().split()))
num_L = 10000000
num_S = 100000
ran = 200

A.sort()
res_A = [[] for _ in range(ran + 1)]
for i in range(0, (num_L * 2 + num_S), num_S):
    for j in A:
        if j < (i - num_L):
            a = i // num_S
            res_A[i // num_S].append(j)
            A.remove(j)
        else:
            pass
## test
for k in res_A:
    if len(k):
        print(k)
    else:
        pass
##
ans = []
for k in res_A:
    if len(k):
        for x in B:
            if k.count(x):
                ans.append(1)
            else:
                ans.append(0)
    else:
        pass

for _3 in ans:
    print(_3, end=" ")
"""
#######################################################################
"""
# 리스트 요소 한번에 괄호 없이 출력
A = [[3, 4], [1, 1], [1, -1], [2, 2], [3, 3]]

for i in A:
    print(*i)
"""
#######################################################################
"""
# stage13 Q05.py
# counting arr
# 정말 천재적인데?
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    max_eliment = 10000
    counting_arr = [0] * (max_eliment + 1)
    for i in range(N):
        input_tmp = int(input())
        counting_arr[input_tmp] += 1
    for i in range(max_eliment + 1):
        if counting_arr[i] != 0:
            for j in range(counting_arr[i]):
                print(i)
"""
#######################################################################
"""
# 빠른 입출력
import sys  # 빠른 입출력을 위한 라이브러리

# 빠른 입출력을 위한 오버로드
input = sys.stdin.readline
print = sys.stdout.write

N = 10  # int(input().rstrip())
for j in range(N):
    print(str(arr[j]) + "\n")
"""
#######################################################################
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

# print 문 방법
 # 1. 특수문자 포함
 print("Let\'s do it")
 # 2. 
"""

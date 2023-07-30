'''
아무 생각없이 작성한 맞는 코드
'''
"""
T = int(input())
n = []
res = []
for i in range(T):
    n.append(map(int,input().split()))
    n[i] = list(n[i])
    res.append(n[i][0] + n[i][1])

for i in range(T):
    print(res[i])
"""
'''
함수를 이용해 입출력을 더 빠르게 진행하게 하는 코드
'''
import sys

T = int(sys.stdin.readline())
n = []
res = []
for i in range(T):
    n.append(map(int,sys.stdin.readline().split()))
    n[i] = list(n[i])
    res.append(n[i][0] + n[i][1])

for i in range(T):
    print(res[i])
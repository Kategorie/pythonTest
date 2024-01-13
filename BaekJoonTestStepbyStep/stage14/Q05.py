import sys

M = int(input())
S = list(map(int, sys.stdin.readline().split()))
N = int(input())
R = list(map(int, sys.stdin.readline().split()))
res = {}
for i in S:
    if i in res:
        res[i] += 1
    else:
        res[i] = 1

for j in R:
    if j in res.keys():
        print(res[j], end=" ")
    else:
        print(0)

import sys

M = int(input())
S = list(map(int, sys.stdin.readline().split()))
N = int(input())
R = list(map(int, sys.stdin.readline().split()))
res = {}
for i in S:
    if i in res.keys():
        res[i] += 1
    else:
        res[i] = 1

for j in R:
    print(res[j], end=" ")

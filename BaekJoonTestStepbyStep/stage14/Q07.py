import sys

print = sys.stdout.write


tmp = 0
N, M = map(int, input().split())
S = set(map(int, sys.stdin.readline().split()))
R = set(map(int, sys.stdin.readline().split()))

for k in R:
    if k not in S:
        tmp += 1

for r in S:
    if r not in R:
        tmp += 1


print(str(tmp))

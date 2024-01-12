import sys

print = sys.stdout.write

res = {}
S = set()
R = set()
tmp = -1
N, M = map(int, input().split())

for j in range(N):
    S.add(sys.stdin.readline().rstrip())

for j in range(M):
    R.add(sys.stdin.readline().rstrip())

for k in R:
    if k in S:
        tmp += 1
        res[tmp] = k


print(str(len(res)) + "\n")
ans = list(res.values())
ans.sort()
for i in ans:
    print(str(i) + "\n")

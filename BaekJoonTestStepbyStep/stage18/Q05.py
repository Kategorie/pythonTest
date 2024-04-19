import sys
import collections

N, M = map(int, sys.stdin.readline().split())
data = []
for _ in range(N):
    data.append(sys.stdin.readline().rstrip())

tmp_D = []
for i in range(N):
    if M <= len(data[i]):
        tmp_D.append(data[i])

res1 = []
res2 = []
tmp_D_c = collections.Counter(tmp_D)
tmp_D_c_k = list(tmp_D_c.keys())
tmp_D_c_v = list(tmp_D_c.values())
t = sorted(tmp_D_c_v)
for j in range(1, len(tmp_D_c_v)):
    if t[j - 1] == t[j]:
        res1.append(tmp_D_c_k[j - 1])
    else:
        res2.append(tmp_D_c_k[j - 1])

res1.sort(key=lambda x: len(x))
res2.sort(key=lambda x: len(x))

for y in res1 + res2:
    print(y)

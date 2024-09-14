import collections
import sys

N = int(input())

A = []
for _ in range(N):
    A.append(int(sys.stdin.readline()))

print(round((sum(A) / N) + 0.0000001))

A.sort()
print(A[N // 2])

dict_a = collections.Counter(A)
tmp_k = list(dict_a.keys())
tmp_v = list(dict_a.values())
t = sorted(tmp_v)
tmp = []
for j in range(len(tmp_v)):
    if t[-1] == tmp_v[j]:
        tmp.append(tmp_k[j])
tmp.sort()
if len(tmp) == 1:
    print(tmp[0])
elif 1 < len(tmp):
    print(tmp[1])

print(A[-1] - A[0])

"""
뱅커스 라운딩
input
3
0
-1
output
-1
-1
-1
-1
1
"""

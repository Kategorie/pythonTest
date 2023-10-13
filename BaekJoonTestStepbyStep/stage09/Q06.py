# 어떤 자연수 N이 있을 때, N의 제곱근까지만 나누어 보면 소인수분해가 가능.
# 시간 초과...
import math

tmp = [] # 임시 리스트
sol = [] # 소수 리스트
ans = []
A = 100000000
N = int(input())
if N == 1:
    print()
else:
    A = math.sqrt(float(N))

for k in range(N):
    # 소수 구하는 코드
    if k <= 1:
        continue
    elif A < k:
        break
    for i in range(1, k + 1):
        if k % i == 0:
            tmp.append(i)
        else:
            pass     
    if len(tmp) <= 2:
        sol.append(k)
    tmp = []

for ii in sol:
    while True:
        ansA, ansB = divmod(N, ii)
        if ansB == 0:
           ans.append(ii)
           N = ansA
        else:
            break

if N < 2:
    pass
else:
    ans.append(N)

ans.sort()
for iii in ans:
    print(iii)
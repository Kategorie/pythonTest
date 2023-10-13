tmp = [] # 임시 리스트
sol = [] # 소수 리스트
M = int(input())
N = int(input())

for k in range(M, N + 1):
    # 소수 구하는 코드
    if k == 1:
        continue
    for i in range(1, k + 1):
        if k % i == 0:
            tmp.append(i)
        else:
            pass     
    if len(tmp) <= 2:
        sol.append(k)
    tmp = []
    
if len(sol) > 0:
    print(sum(sol))
    sol.sort()
    print(sol[0])
else:
    print(-1)

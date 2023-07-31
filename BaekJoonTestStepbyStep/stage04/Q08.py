N = 10  # 10개 입력
M = 42  # 나머지 개수

A = []
cnt = 0
for z in range(N):
    a = int(input())
    A.append(a % 42)

for x in range(M):
    if A.count(x) == 1:
        cnt += 1
    elif A.count(x) > 1:
        cnt += 1

print(cnt)

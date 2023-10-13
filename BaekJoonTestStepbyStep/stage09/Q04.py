N = int(input())
n = []
tmp = []
cnt = 0

n = list(map(int, input().split()))
for j in n: # 소수 구하는 코드
    if j == 1:
        continue
    for i in range(1, j + 1):
        if j % i == 0:
            tmp.append(i)
        else:
            pass
    if len(tmp)  <= 2:
        cnt += 1
    tmp = []

print(cnt)
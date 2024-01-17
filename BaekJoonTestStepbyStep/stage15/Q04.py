N = int(input())

L = []
tmp1 = 0
tmp2 = 0
num = 1000000000
flag = True
for i in range(N):
    L.append(int(input()))
    if flag:
        flag = False
        continue
    else:
        res = L[i] - L[i - 1]
        if res < num:
            num = res

cnt = ((L[len(L) - 1] - L[0]) // num) + 1
ans = cnt - len(L)
print(ans)

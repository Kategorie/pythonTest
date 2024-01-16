N = int(input())


L = []
tmp1 = 0
tmp2 = 0
num = 1000000000
flag = True
for i in range(N - 1):
    L.append(int(input()))
    if flag: 
        flag = False 
        continue
    else:
        res = L[i-1] - L[i]
        if res < num:
            num = res

S = num * j for j in range(2, N - 1))


print()

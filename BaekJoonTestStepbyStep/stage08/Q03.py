T = int(input())
N = []
tmp = []
res = []
quarter = 25
dime = 10
nickel = 5
penny = 1

for i in range(T):
    N.append(int(input()))

for j in N:
    a, j = divmod(j, quarter) #몫 / #나머지
    
    tmp.append(a)
    a, j = divmod(j,dime)
    tmp.append(a)
    a, j = divmod(j,nickel)
    tmp.append(a)
    a, j = divmod(j,penny)
    tmp.append(a)

    res.append(tmp)
    tmp = []
    
for k in res:
    for kk in range(len(k)):
        print(k[kk], end=" ")
    print()
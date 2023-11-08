a, b = map(int, input().split())
res = []
ans = []
tmp = []
if a == b:
    ans.append(a)
else:
    c = max(a, b)
    d = min(a, b)
    for j in range(1, (c - d) + 1):
        tmp1, tmp2 = divmod(c - d, j)
        if tmp2 == 0:
            res.append(tmp1)
    res.sort()
    for k in res:
        if a % k == 0 and b % k == 0:
            tmp.append(int((a * b) / k))  # 공배수
    tmp.sort()
    ans.append(tmp[0])
    tmp = []
    res = []

for x in ans:
    print(x)

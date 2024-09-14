N = int(input())
data = []
for _ in range(N):
    data.append(input())

cnt = 0
res = []
tmp = []
for i in range(1, N):
    if data[i] == "ENTER":
        res.append(tmp)
        tmp = []
    else:
        tmp.append(data[i])

res.append(tmp)

for j in res:
    cnt += len(set(j))

print(cnt)

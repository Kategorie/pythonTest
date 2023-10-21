N, M = map(int, input().split())
S = list(map(int, input().split()))
sum = []
ans = 0
for i in range(len(S)):
    for j in range(i + 1, len(S)):
        for k in range(j + 1, len(S)):
            sum.append(S[i] + S[j] + S[k])
sum.sort()
for x in sum:
    if x <= M:
        ans = x
    else:
        continue
print(ans)

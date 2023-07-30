X = int(input())
N = int(input())
n = []
res = 0
for i in range(N):
    n.append(map(int,input().split()))
    n[i] = list(n[i])
    res += n[i][0] * n[i][1]

if res == X:
    print("Yes")
else:
    print("No")


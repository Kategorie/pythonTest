N = int(input())
Nary = input()

Nary = list(map(int, Nary))
res = 0
for i in range(N):
    res += Nary[i]
print(res)

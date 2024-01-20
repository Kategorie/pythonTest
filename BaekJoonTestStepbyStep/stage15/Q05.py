N = int(input())
L = []
for _ in range(N):
    L.append(int(input()))

for i in range(N):
    for j in range(L[i], L[i]*3):
        if L[i] == 1:
            pass
        else:
            
A = {}
N = 28
for y in range(1, N + 3):
    A[y] = 0

for z in range(1, N + 1):
    a = int(input())
    A[a] = a

for x in range(1, N + 3):
    if A[x] == 0:
        print(x)

A = {}
N, M = map(int, input().split())

for x in range(M):
    i, j, k = map(int, input().split())
    for y in range(i, j + 1):
        A[y] = k
for q in range(1, N + 1):
    print(A.get(q, 0), end=" ")

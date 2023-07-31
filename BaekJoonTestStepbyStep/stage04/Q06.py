A = {}
N, M = map(int, input().split())

for z in range(1, N + 1):
    A[z] = z
for x in range(M):
    i, j = map(int, input().split())
    A[i], A[j] = A[j], A[i]

for q in range(1, N + 1):
    print(A.get(q), end=" ")

N = int(input())
res = 0
A = list(map(int, input().split()))
M = max(A)
for i in range(len(A)):
    A[i] = A[i]/M*100
    res += A[i]

print(res/N)
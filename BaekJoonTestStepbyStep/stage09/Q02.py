N, K = map(int, input().split())
A= []
for i in range(1, N+1):
    if N % i == 0:
        A.append(i)
    else:
        pass
A.sort()
if K <= len(A):
    print(A[K-1])
else:
    print('0')
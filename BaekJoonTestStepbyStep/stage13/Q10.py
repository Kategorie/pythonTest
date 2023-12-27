N = int(input())
num = 200
A = [[] for _ in range(num + 1)]  # counting arr
tmp = []
res = []

for i in range(N):
    tmp = list(map(str, input().split()))
    A[int(tmp[0])].append(tmp)

for j in range(1, num + 1):
    if len(A[j]) < 1:
        pass
    else:
        for k in A[j]:
            print(k[0], k[1])

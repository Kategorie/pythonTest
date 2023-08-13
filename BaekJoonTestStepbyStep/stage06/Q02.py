S = [1,1,2,2,2,8]
A = list(map(int,input().split()))
for i in range(len(S)):
    print(S[i] - A[i], end=" ")
N,M = map(int, input().split())
A = []
B = []
C = []
#c = []
for i in range(N):
    A.append(list(map(int,input().split())))
for ii in range(N):
    B.append(list(map(int,input().split())))

for j in range(N):
    for jj in range(M):
        print(A[j][jj]+ B[j][jj], end=" ") 
    print()
'''
for j in range(N):
    for jj in range(M):
        c.append(A[j][jj]+ B[j][jj]) 
    C.append(c)
    c = []
for k in range(N):
    print(C[k])
'''
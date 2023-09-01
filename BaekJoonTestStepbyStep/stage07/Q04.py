N = int(input())
X = []
Y = []
tmp_X1 = []
tmp_X2 = []
tmp_Y1 = []
tmp_Y2 = []
A = 10
for i in range(N):
    x,y = map(int, input().split())
    X.append(x)
    Y.append(y)
    x,y = 0

for i in range(len(X)): # 기준값
    for ii in range(len(X)): # 로테이션
        if  X[ii] < X[i] and X[i] < (X[ii] + A):
            tmp_X1.append(i)
    for iii in range(len(X)): # 로테이션
        if  (X[iii]+A) < (X[i]+A) and X[i] < (X[iii] + A):
            tmp_X2.append(X[i-1])

for j in Y: # 기준값
    for jj in range(len(Y)): # 로테이션
        if  Y[jj] < j and j < (Y[jj] + 10):
            tmp_Y1.append(j)

res = (tmp_X2[i] - tmp_X1[i]) * (tmp_Y2[i] - tmp_Y1[i])

ans = (N * 100) + res
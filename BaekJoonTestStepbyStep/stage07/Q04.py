N = int(input())
m = 101
n = 10
cnt = 0
A = [[0] * m for _ in range(m)] # 컴프리헨션(Comprehension)
for i in range(N):
    x,y = map(int,input().split())
    for j in range(n):
        for k in range(n):
            A[x+j][y+k] = 1

for ii in range(m):
    cnt += A[ii].count(1)
    
print(cnt)


'''
# 색종이의 겹치는 부분의 꼭지점을 이용해 계산해서 풀려고 했지만 색종이가 겹치는 부분이 많아질 수록 불가능한 방법이라고 생각되어 작성하다가 말음.
N = int(input()) # 색종이 수
X = []
Y = []
tmp_X1 = []
tmp_X2 = []
tmp_Y1 = []
tmp_Y2 = []
A = 10
for i in range(N):
    x,y = map(int, input().split()) # 색종이를 붙인 위치
    X.append(x)
    Y.append(y)
    x,y = 0

for i in range(len(X)): # 기준값
    for ii in range(len(X)): # 로테이션 (기존 X값에서 겹치는 부분 찾기)
        if  X[ii] < X[i] and X[i] < (X[ii] + A):
            tmp_X1.append(i)
    
for iii in range(len(X)):    
    for iiii in range(len(tmp_X1)): # 로테이션 (크기 10짜리 X값에서 겹치는 부분 찾기)
        if  (X[iii]+A) < (tmp_X1[iiii]+A) and X[i] < (X[i] + A):
            tmp_X2.append(X[i-1])

for j in Y: # 기준값
    for jj in range(len(Y)): # 로테이션
        if  Y[jj] < j and j < (Y[jj] + 10):
            tmp_Y1.append(j)

res = (tmp_X2[i] - tmp_X1[i]) * (tmp_Y2[i] - tmp_Y1[i])

ans = (N * 100) + res
'''
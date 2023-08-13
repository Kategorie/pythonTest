T = int(input())
RS = []
P = []
A = []
for jj in range(T):
    a,b = input().split()
    RS.append([a,b])

for i in range(T): # 2
    for j in range(len(RS[i][1])): # 2
        for k in range(int(RS[i][0])): # 3
            A.append(RS[i][1][j])
    P.append(A)
    A = []

for ii in range(len(P)):
    for iii in range(len(P[ii])):
        print(P[ii][iii], end="")
    print()
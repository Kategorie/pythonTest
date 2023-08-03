T = 2#int(input())
RS = []
P = []

for jj in range(T):
    RS.append([3, 'ABC'])#input()

for i in range(T):
    for j in range(len(RS)):
        for k in range(RS[i][0]):
            P.append(RS[i][1][k])


for ii in range(len(P)):
    print(P[ii])
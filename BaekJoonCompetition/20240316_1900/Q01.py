import sys

data = []

for _ in range(10):
    data.append(sys.stdin.readline().rstrip().split())

colored = ""

for i in range(10):
    colored = data[i][0]
    flag = False
    for j in range(10):
        aa = data[i][j]
        if colored == data[i][j]:
            flag = True
        else:
            flag = False
            break
    if flag:
        print("1")
        exit(0)
    colored = data[1][i]
    for k in range(10):
        bb = data[k][i]
        if colored == data[k][i]:
            flag = True
        else:
            flag = False
            break
    if flag:
        print("1")
        exit(0)
if flag == 0:
    print("0")

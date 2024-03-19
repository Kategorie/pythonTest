import sys


data = []

M = int(sys.stdin.readline())
for i in range(M):
    order = sys.stdin.readline().split()  # 이거 시간이랑 상관관계가 커서 재밌네

    if order[0] == "1":
        data.append(order[1])
    elif order[0] == "2":
        if len(data):
            print(data.pop())
        else:
            print("-1")
    elif order[0] == "3":
        print(len(data))
    elif order[0] == "4":
        if len(data):
            print("0")
        else:
            print("1")
    elif order[0] == "5":
        if len(data):
            print(data[-1])
        else:
            print("-1")
    else:
        pass

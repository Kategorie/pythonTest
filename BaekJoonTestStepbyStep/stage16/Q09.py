import sys
from collections import deque

N = int(input())
res_deque = deque()

for _ in range(N):
    com = sys.stdin.readline().rstrip().split()

    if com[0] == "1":
        res_deque.appendleft(com[1])
    elif com[0] == "2":
        res_deque.append(com[1])
    elif com[0] == "3":
        if len(res_deque):
            print(res_deque.popleft())
        else:
            print("-1")
    elif com[0] == "4":
        if len(res_deque):
            print(res_deque.pop())
        else:
            print("-1")
    elif com[0] == "5":
        print(len(res_deque))
    elif com[0] == "6":
        if len(res_deque):
            print("0")
        else:
            print("1")
    elif com[0] == "7":
        if len(res_deque):
            print(res_deque[0])
        else:
            print("-1")
    elif com[0] == "8":
        if len(res_deque):
            print(res_deque[-1])
        else:
            print("-1")
    else:
        print("err")

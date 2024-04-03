import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
queue = deque()
num_1 = 1
num_0 = 0
num_0_1 = -1
q_app = queue.append
for i in range(N):
    inp = sys.stdin.readline().rstrip().split()

    if inp[0] == "push":
        q_app(inp[1])
    elif inp[0] == "pop":
        if len(queue):
            print(queue.popleft())
        else:
            print(num_0_1)
    elif inp[0] == "size":
        print(len(queue))
    elif inp[0] == "empty":
        if len(queue):
            print(num_0)
        else:
            print(num_1)
    elif inp[0] == "front":
        if len(queue):
            print(queue[0])
        else:
            print(num_0_1)
    elif inp[0] == "back":
        if len(queue):
            print(queue[-1])
        else:
            print(num_0_1)
    else:
        pass

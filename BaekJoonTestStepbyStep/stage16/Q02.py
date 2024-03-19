import sys


data = []
N = int(sys.stdin.readline())
for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(data) < 1:
            continue
        else:
            del data[len(data) - 1]
    else:
        data.append(num)

print(sum(data))

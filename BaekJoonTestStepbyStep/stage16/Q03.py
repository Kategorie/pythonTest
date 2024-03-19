import sys

N = int(sys.stdin.readline())

for _ in range(N):
    data = list(sys.stdin.readline())
    cnt = 0

    for i in data:
        if i == "(":
            cnt += 1
        elif i == ")" and cnt != 0:
            cnt -= 1
        elif i == ")" and cnt == 0:
            cnt = 1
            break

    if cnt == 0:
        print("YES")
    else:
        print("NO")

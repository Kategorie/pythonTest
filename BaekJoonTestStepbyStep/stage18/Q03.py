import sys

N = int(input())

data = ["ChongChong"]
for _ in range(N):
    a, b = sys.stdin.readline().split()
    for d in data:
        if d == a:
            data.append(b)
            break
        elif d == b:
            data.append(a)
            break
        else:
            continue

print(len(set(data)))

# 총총 포함

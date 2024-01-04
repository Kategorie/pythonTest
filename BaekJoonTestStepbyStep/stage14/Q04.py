import sys


def bisearch(target, data, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if isinstance(target, int):
        if data[mid][1] == target:
            return data[mid][0]
        elif data[mid][1] < target:
            start = mid + 1
        else:
            end = mid - 1
    else:
        if data[mid][0] == target:
            return data[mid][1]
        elif data[mid][0] < target:
            start = mid + 1
        else:
            end = mid - 1

    return bisearch(target, data, start, end)


N, M = map(int, sys.stdin.readline().split())
S = []
R = []
res = []

for _ in range(N):
    S.append([sys.stdin.readline().rstrip(), _ + 1])

for _ in range(M):
    R.append(sys.stdin.readline().rstrip())

data = []
S_dec = sorted(S, key=lambda x: x[1])
S_ori = sorted(S)
for i in R:
    if i[0].isdecimal():
        data = S_dec
        i = int(i)
    else:
        data = S_ori
    res.append(bisearch(i, data, 0, len(data)))

for j in res:
    print(j)

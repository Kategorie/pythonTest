import sys


def bisearch(target, data, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if data[mid] == target:
        return mid
    elif data[mid] < target:
        start = mid + 1
    else:
        end = mid - 1

    return bisearch(target, data, start, end)


print = sys.stdout.write

N = int(input())
S = sys.stdin.readline().rstrip().split()
M = int(input())
R = sys.stdin.readline().rstrip().split()
res = []
max_eliment = 20000000
arr = []
counting_res = [0] * (max_eliment + 1)

for j in S:  # S 기수 정렬
    counting_res[int(j)] += 1

for k in R:  # R 값을 기준으로 S에서 이진탐색
    res.append(bisearch(k, counting_res, 1, len(counting_res)))

for i in res:
    print(str(i) + " ")

def bisearch(target, data, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if data[mid] == target:
        return mid
    elif data[mid] < target:
        start = mid + 1
    else:
        end = mid - 1

    return bisearch(target, data, start, end)


n = int(input())
S = []
R = []
for _ in range(n):
    tmp1, tmp2 = map(str, input().split())
    if tmp2 == "enter":
        S.append(tmp1)
    else:
        R.append(tmp1)

S.sort()
for j in R:
    idx = bisearch(j, S, 0, len(S) - 1)
    del S[idx]

# S.sort(reverse=True)
for i in S[::-1]:
    print(i)

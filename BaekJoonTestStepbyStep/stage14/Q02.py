def bisearch(target, data, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if data[mid] == target:
        return 1
    elif data[mid] < target:
        start = mid + 1
    else:
        end = mid - 1

    return bisearch(target, data, start, end)


N, M = 5, 11  # map(int, input().split())
S = [
    "baekjoononlinejudge",
    "startlink",
    "codeplus",
    "sundaycoding",
    "codingsh",
]
req = [
    "baekjoon",
    "codeplus",
    "codeminus",
    "startlink",
    "starlink",
    "sundaycoding",
    "codingsh",
    "codinghs",
    "sondaycoding",
    "startrink",
    "icerink",
]

"""
for _ in range(N):
    S.append(input())

for _ in range(M):
    req.append(input())
"""
S.sort()
res = 0
for i in req:
    res += bisearch(i, S, 0, len(S) - 1)
print(res)

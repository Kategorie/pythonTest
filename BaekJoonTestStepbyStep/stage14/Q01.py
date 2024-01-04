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


N = int(input())
# A = [6, 3, 2, 10, -10]
A = list(map(int, input().split()))

M = int(input())
# B = [10, 9, -5, 2, 3, 4, 5, -10]
B = list(map(int, input().split()))

A.sort()
for i in B:
    print(bisearch(i, A, 0, len(A) - 1), end=" ")

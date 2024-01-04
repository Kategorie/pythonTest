# 정렬된 배열만 넣어야함. 전달된 배열의 인덱스를 반환함
def bisearch(target, data, start, end):
    if start > end:  # 범위를 넘어도 못찾는다면 -1을 반환
        return -1
    mid = (start + end) // 2
    if data[mid] == target:
        return mid
    elif data[mid] < target:
        start = mid + 1
    else:
        end = mid - 1

    return bisearch(target, data, start, end)


N = int(input())
A = list(map(int, input().split()))

B = list(set(A))
B.sort()
for i in A:
    idx = bisearch(i, B, 0, len(B) - 1)
    print(idx, end=" ")

"""
2 4 -10 4 -9

2 4 -10 -9

-10 -9 2 4

-10 -9 2 4 4

  0  1 2 3 4
# 자체적으로 이분 탐색을 개조해 봤는데 시간이 오래걸리드라
def bisearch(s_num, str, idx_len):
    ls = int(len(str) / 2)
    if str[ls] < s_num:
        res = str[ls:]
    elif str[ls] == s_num:
        return ls + idx_len
    else:
        res = str[:ls]
        ls = 0

    return bisearch(s_num, res, ls)


N = int(input())
A = list(map(int, input().split()))

B = list(set(A))
B.sort()
res = []
for i in A:
    idx = bisearch(i, B, 0)
    print(idx, end=" ")
"""

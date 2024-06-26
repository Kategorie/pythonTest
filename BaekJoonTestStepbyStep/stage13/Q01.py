# 삽입정렬
N = int(input())
list_A = []

for i in range(N):
    list_A.append(int(input()))

for j in range(1, N):  # 현재값
    for k in range(j):  # 비교할 정렬값
        if list_A[k] < list_A[j]:
            continue
        else:
            list_A.insert(k, list_A[j])
            del list_A[j + 1]
            break

for x in range(len(list_A)):
    print(list_A[x])
"""
# 버블정렬
N = int(input())
list_A = []

for i in range(N):
    list_A.append(int(input()))

for j in range(N - 1):
    for k in range(N - 1 - j):
        if list_A[k + 1] < list_A[k]:
            tmp = list_A[k]
            list_A[k] = list_A[k + 1]
            list_A[k + 1] = tmp
        else:
            continue

for x in range(len(list_A)):
    print(list_A[x])
"""

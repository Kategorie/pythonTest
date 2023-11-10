N = []
n = int(input())

for i in range(n):
    N.append(int(input()))

for j in range(1, len(N)):  # 비교대상
    for k in range(j):  # 정렬된 리스트
        if N[k] < N[j]:
            continue
        else:
            N.insert(k, N[j])
            del N[j + 1]

for x in N:
    print(x)

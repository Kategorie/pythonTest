A = {}
N, M = map(int, input().split())
'''
IndexError: list assignment index out of range
A를 딕셔너리가 아닌 리스트로 지정하면 이러한 오류가 나온다.
빈 리스트에 인덱스를 지정했을 때 나오는 에러이다.
'''
for z in range(0, N + 1):
    A[z] = z
for x in range(M):
    i, j = map(int, input().split())
    for y in range(j):
        if i == j or i > j:
            break
        else:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1


for q in range(1, N + 1):
    print(A.get(q), end=" ")
N = 5  # int(input())
A = [[0, 4], [1, 2], [1, -1], [2, 2], [3, 3]]  # []
# for _ in range(N):
#    A.append(list(map(int, input().split())))

A.sort(key=lambda x: (x[1], x[0]))
for i in A:
    for j in i:
        print(j, end=" ")
    print()

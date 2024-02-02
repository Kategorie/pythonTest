def Eratos(data, M, N):
    for i in range(N + 1):
        if i == 0 or i == 1:
            data[i] = False
        else:
            if data[i]:
                j = 2
                while i * j <= N:
                    data[i * j] = False
                    j += 1


if __name__ == "__main__":
    M, N = map(int, input().split())
    res = [True] * (N + 1)
    Eratos(res, M, N)

    for i in range(M, N + 1):
        if res[i]:
            print(i)

"""
# 시간 초과
def Eratos(data, M, N):
    for i in range(M, N + 1):
        flag = False
        if i == 0 or i == 1:
            continue
        elif i == 2 or i == 3:
            data[i] = True
            continue
        else:
            for j in range(2, i):
                if i % j == 0:
                    flag = False
                    break
                else:
                    flag = True
            if flag:
                data[i] = True


if __name__ == "__main__":
    M, N = map(int, input().split())
    res = [False] * N
    Eratos(res, M, N)

    for i in range(len(res)):
        if res[i]:
            print(i)
"""

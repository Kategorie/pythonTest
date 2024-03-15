def execute():

    N = int(input())  # 2100000000  # max(inp)  #
    cnt = 0
    for j in range(1, N + 1):
        if j * j <= N:
            cnt += 1
        else:
            break
    print(cnt)


execute()

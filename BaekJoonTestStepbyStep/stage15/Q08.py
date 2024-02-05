def Eratos(data, num):
    for i in range((num * 2) + 1):
        if i == 0 or i == 1:
            data[i] = False
        else:
            if data[i]:
                j = 2
                while i * j <= num * 2:
                    data[i * j] = False
                    j += 1


if __name__ == "__main__":
    N = int(input())

    inp = []
    for i in range(N):
        inp.append(int(input()))

    r_m = max(inp)
    res = [True] * ((r_m * 2) + 1)
    Eratos(res, r_m)

    for j in inp:
        for k in range(2, int(j / 2) + 1):
            if res[k]:
                pass

    for i in inp:
        if inp == 0:
            break
        else:
            cnt = 0
            for j in range(i + 1, (i * 2) + 1):
                if res[j]:
                    cnt += 1
            print(cnt)

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


# test
if __name__ == "__main__":
    N = int(input())

    inp = []
    for i in range(N):
        inp.append(int(input()))

    r_m = max(inp)
    res = [True] * ((r_m * 2) + 1) # 소수만 남는 에라토스 테네스의 체 데이터
    Eratos(res, r_m) # 소수 리스트

    for j in inp:
        for k in range(j):
            if res[k] < j:
                tmp = j - res[k]
                for x in range(tmp):
                    if tmp % x == 0:
                        break # 소수가 아닌 경우
                    else:
            else:
                break # 소수가 input 보다 클 경우

    for i in inp:
        if inp == 0:
            break
        else:
            cnt = 0
            for j in range(i + 1, (i * 2) + 1):
                if res[j]:
                    cnt += 1
            print(cnt)


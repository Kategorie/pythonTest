import time


def Eratos(data, num):
    for i in range(num):
        if i == 0 or i == 1:
            data[i] = False
        else:
            if data[i]:
                j = 2
                while i * j <= num:
                    data[i * j] = False
                    j += 1


def execute():
    time_start = time.time()

    r_m = 2100000000  # max(inp)  #
    res = [True] * (r_m + 1)  # 소수만 남는 에라토스 테네스의 체 데이터
    Eratos(res, r_m)  # 소수 리스트

    time_end = time.time()
    time_result = time_end - time_start
    print(str(time_result))


execute()

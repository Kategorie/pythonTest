import sys
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


# test
# if __name__ == "__main__":
def execute():  # 함수 호출로 하는 경우가 로컬 변수를 써서 그런가 더 빠르게 작업함(시간 단축)
    N = int(sys.stdin.readline())
    """
    inp = []
    for i in range(N):
        inp.append(int(input()))
    """

    time_start = time.time()

    r_m = 1000000  # max(inp)  #
    res = [True] * (r_m + 1)  # 소수만 남는 에라토스 테네스의 체 데이터
    Eratos(res, r_m)  # 소수 리스트
    time_end = time.time()
    time_result = time_end - time_start
    print(str(time_result))

    time_start = time.time()
    for j in range(N):
        cnt = 0
        inp = int(sys.stdin.readline())
        for k in range(inp):
            if res[k]:
                tmp = inp - k  # 입력 값 - 소수
                if res[tmp] and k <= tmp:
                    cnt += 1
            else:
                continue
        print(cnt)
    time_end = time.time()
    time_result = time_end - time_start
    print(str(time_result))


execute()
"""
242
458
88466
77792
999998
2930
22222
57288
229944
485088
242
458
88466
77792
999998
2930
22222
57288
229944
485088
242
458
88466
77792
999998
2930
22222
57288
229944
485088
242
458
88466
77792
999998
2930
22222
57288
229944
485088
242
458
88466
77792
999998
2930
22222
57288
229944
485088
242
458
88466
77792
999998
2930
22222
57288
229944
485088
242
458
88466
77792
999998
2930
22222
57288
229944
485088
242
458
88466
77792
999998
2930
22222
57288
229944
485088
242
458
88466
77792
999998
2930
22222
57288
229944
485088
242
458
88466
77792
999998
2930
22222
57288
229944
485088
"""

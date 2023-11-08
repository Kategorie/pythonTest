# (두 수 A, B의 최소공배수) = A * B / (A, B의 최대공약수)
# 최대공약수는 유클리드 호재법으로 계산하면 쉽게 알 수 있다.
# A-B는 최대공약수 G의 배수이다. 따라서 A-B의 약수 중 최대공약수 G가 있다.
T = int(input())
res = []
ans = []
tmp = []

for i in range(T):
    a, b = map(int, input().split())
    if a == b:
        ans.append(a)
    else:
        c = max(a, b)
        d = min(a, b)
        for j in range(1, (c - d) + 1):
            tmp1, tmp2 = divmod(c - d, j)
            if tmp2 == 0:
                res.append(tmp1)
        res.sort()
        for k in res:
            if a % k == 0 and b % k == 0:
                tmp.append(int((a * b) / k))  # 공배수
        tmp.sort()
        ans.append(tmp[0])
        tmp = []
        res = []

for x in ans:
    print(x)

"""
# 되긴 하는데 특정 케이스에서 시간이 너무 오래걸림
T = int(input())
ans = []
A = []
flag = False

for i in range(T):
    a, b = map(int, input().split())
    c = min(a, b)
    if abs(a - b) < c:
        for ii in range(1, max(a, b) + 1):
            for j in range((ii * 10) - 9, ii * 10):
                A.append(b * j)
            for k in range((ii * 10) - 9, ii * 10):
                A.append(a * k)

            for x in A:
                if A.count(x) == 2:
                    ans.append(x)
                    flag = True
                    break
            if flag:
                break
    else:
        ans.append(a * b)

for y in ans:
    print(y)
"""

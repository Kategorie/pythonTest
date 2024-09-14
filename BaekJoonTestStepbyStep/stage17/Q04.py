def fact(num):
    res = 1
    for i in range(1, num + 1):
        res = res * i
    return res


N, K = map(int, input().split())
if N == 1 and (K == 0 or K == 1):
    print("1")
else:
    print(fact(N) // (fact(N - K) * fact(K)))

"""
이항계수 = 순서 없는 경우의 수
이항 = 뽑거나 뽑지 않거나 2가지 경우
(n,k) = nCk = n!/(n-k)!k!
"""

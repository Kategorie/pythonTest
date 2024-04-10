def fact(num):
    res = 1
    for i in range(1, num + 1):
        res = res * i
    return res


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(fact(M) // (fact(N) * (fact(M - N))))


"""
겹치지 않게 한다는 문장에 너무 정신이 팔렸는데
어짜피 큰 수에서 작은 수의 "경우의 수"를 찾는 문제이기 때문에
어떤 순서로 찾던 겹치진 않음
어짜피 선을 잇는건 대충 안겹치게만 이으면 되니까
"""

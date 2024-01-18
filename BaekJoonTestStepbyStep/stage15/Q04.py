# 두 수의 최대공약수 라는 것은 원점을 기준으로 해당 값이 최대공약수의 간격으로 일정한 거리를 갖는다는 뜻이다.
# 즉, 4와 6의 최대공약수는 2인데, 4는 2의 간격으로 2번 나눠질 수 있고, 6도 2의 간격으로 3번 나눠질 수 있다는 의미이다.


def euclideean(small, big):
    res = big % small
    if res == 0:
        return small
    else:
        return euclideean(res, small)


# 이 문제에서 나눠져야 할 구간은 주어진 값 사이의 공간이다. 즉, 주어진 값을 나누는게 아니라 주어진 값 사이의 간격을 나눠야 한다. (중요함)
# 이 말은 즉, ex/ 1 3 7 13 의 값을 나눌게 아니라 이 값 사이의 간격을 나눠야 한다. 2 4 6
if __name__ == "__main__":
    N = int(input())
    L = []
    R = []
    for i in range(N):
        L.append(int(input()))
        if i > 0:
            R.append(L[i] - L[i - 1])

    for j in range(len(R)):
        gcd = euclideean(R[j - 1], L[j])
        R.append(gcd)

    print()

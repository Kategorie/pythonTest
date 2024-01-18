def euclideean(small, big):
    res = big % small
    if res == 0:
        return small
    else:
        return euclideean(res, small)


if __name__ == "__main__":
    N = int(input())
    L = []
    gcd = 0
    R = []
    for i in range(N):
        L.append(int(input()))
        if i > 0:
            gcd = euclideean(L[i - 1], L[i])
            R.append(gcd)

    print()

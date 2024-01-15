import sys

if __name__ == "__main__":
    S = sys.stdin.readline().rstrip()

    start = 0
    end = 1
    res = set()
    for i in range(len(S)):
        for j in range(i, len(S)):
            tmp = S[start + i : end + j]
            res.add(tmp)

    print(len(res))

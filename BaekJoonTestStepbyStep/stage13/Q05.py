import sys  # 빠른 입출력을 위한 라이브러리

# 빠른 입출력을 위한 오버로드
input = sys.stdin.readline
print = sys.stdout.write


def counting(arr, K):
    m = max(K)
    C = [0] * (m + 1)
    for a in arr:
        C[a] += 1
    for i in range(1, m + 1):
        C[i] += C[i - 1]
    result = [0] * len(arr)
    for a in arr:
        result[C[a] - 1] = a
        C[a] -= 1
    return result


if __name__ == "__main__":
    N = 10  # int(input().rstrip())
    n = [10, 2, 4, 5, 3, 5, 2, 6, 1, 2]
    # for i in range(N):
    #    n.append(int(input().rstrip()))

    counting(n, N)

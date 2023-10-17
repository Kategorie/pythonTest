S = list(map(int, input().split()))
S.sort()
while True:
    if S[2] < S[0] + S[1]:
        print(sum(S))
        break
    else:
        S[2] -= 1

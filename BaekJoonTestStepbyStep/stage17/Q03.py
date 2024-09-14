N = int(input())

res = 1

if N == 1:
    print("1")
else:
    for i in range(1, N + 1):
        res = res * i
    print(res)

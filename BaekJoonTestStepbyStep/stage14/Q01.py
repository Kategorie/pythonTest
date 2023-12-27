N = 5  # int(input())
A = [6, 3, 2, 10, -10]
# A = list(map(int, input().split()))

M = 8  # int(input())
B = [10, 9, -5, 2, 3, 4, 5, -10]
# B = list(map(int, input().split()))

num_L = 10000000
num_S = 100000
ran = 200

res_B = [[] for _ in range(ran + 1)]
for i in range(0, (num_L * 2 + num_S), num_S):
    for j in B:
        if j < (i - num_L):
            res_B[i // num_S].append(j)
            A.remove(j)
        else:
            pass
## test
for k in res_B:
    if len(k):
        print(k)
    else:
        pass
##
ans = []
for k in res_A:
    if len(k):
        for x in B:
            if k.count(x):
                ans.append(1)
            else:
                ans.append(0)
    else:
        pass

for _ in ans:
    print(_, end=" ")

a, b = map(int, input().split())  # 분자 분모
c, d = map(int, input().split())


"""
# 알고리즘은 맞는데 시간 초과됨
a, b = map(int, input().split())  # 분자 분모
c, d = map(int, input().split())
# a c 2 3
# b d 7 5
A = a * d
B = b * d  # B = D
C = c * b

res1 = A + C
res2 = B

for i in range(1, res1 + 1):
    if res1 % i == 0 and res2 % i == 0:
        res1 /= i
        res2 /= i

print(int(res1), int(res2))
"""

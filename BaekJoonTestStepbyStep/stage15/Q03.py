a, b = map(int, input().split()) # 분자 분모
c, d = map(int, input().split())

A = a * d
B = b *d # B = D
C = c * b

res1 = A + C
res2 = B

for i in range(res1):
    if res1 % i == 0 and res2 % i == 0:
        
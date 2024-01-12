import math
import sys

S = sys.stdin.readline().rstrip()
res = set()
for i in range(2, len(S)+1):
    tmp = S[:i]
    math.factorial(len(tmp))


print(len(S) + len(res))

5 4 3 2 1 의 합에서 중복을 제거

# for문과 count로 간단하게 구현하는 것도 있다.
import math

A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())
C1, C2 = map(int, input().split())
D1 = 0
D2 = 0

if A1 == B1:
    D1 = C1
elif B1 == C1:
    D1 = A1
else:  # A1 == C1
    D1 = B1

if A2 == B2:
    D2 = C2
elif B2 == C2:
    D2 = A2
else:  # A2 == C2
    D2 = B2

print(D1, D2)

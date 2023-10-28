a, b, c, d, e, f = map(int, input().split())

x = (c * e - f * b) // (a * e - d * b)
y = (c * d - a * f) // (b * d - a * e)

print(x, y)

"""
# Fraction 함수를 사용해서 가감법을 이용해 연립방정식을 풀 수 있지만 0 체크가 안됨
# 너무 어렵게 생각하지 말고 걍 연립방정식을 풀어보면 알 수 있음
# x와 y에 대한 일방항을 구하면 됨
from fractions import Fraction

a, b, c, d, e, f = map(int, input().split())

cal_b = Fraction(b, a)
cal_c = Fraction(c, a)
cal_e = Fraction(e, d)
cal_f = Fraction(f, d)

ans_y1 = cal_b - cal_e
ans_y2 = cal_c - cal_f

ans_y = ans_y2 * Fraction(1, ans_y1)

ans_x = cal_c - (cal_b * ans_y)

print(int(ans_x), int(ans_y))
"""

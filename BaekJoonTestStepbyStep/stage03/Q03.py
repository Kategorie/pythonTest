""" 
'''
    재귀함수 이용(다만 파이썬 재귀 한계 범위를 넘지 못함
    약 1500~2000 사이인듯?)
    다만, 아래 코드를 이용해 재귀 한계를 늘릴 수 있음
    import sys
    sys.setrecursionlimit(10**number)
''' 
"""
import sys
sys.setrecursionlimit(10**5)

class ddd():
    res = 0
    def inp(res):
        ddd.res = res

    def comp(res,a):
        if a <= 0:
            ddd.inp(res)
            return
        else:
            res+=a+(a-1)
            ddd.comp(res,a-2)

a = int(input())
ddd.comp(ddd.res,a)
print(ddd.res)

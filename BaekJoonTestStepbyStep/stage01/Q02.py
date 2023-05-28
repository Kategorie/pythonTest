# from stage01 import *

class Calculator:
    n1 = 0
    n2 = 0
    def __init__(self) -> None: # -> 는 리턴값이 어떤지 명시해주기 위해서 사용한다. 
        pass

    def sum(self, n1, n2) -> int:
        return n1 + n2
    
    def printResult(self, n1, n2, result) : 
        # print("{} + {} = {}", format(n1, n2, result)) # 기본 형태
        print(f"{n1} + {n2} = {result}") # 간편 f-string

if __name__ == '__main__' :
    
    a = int(input("정수형 숫자를 입력하세요 : "))
    b = int(input("정수형 숫자를 입력하세요 : "))
    
    calc = Calculator()
    r = calc.sum(a,b)
    calc.printResult(a,b,r)


#def sum():
#    a, b = map(int, input().split())
#    print(f"{a+b}")
#
#sum()
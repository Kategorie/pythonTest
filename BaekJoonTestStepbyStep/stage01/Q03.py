class calc:
    a = 0
    b = 0

    def __init__(self) -> None:
        pass

    def inp(a1, b1):
        cal.a = a1
        cal.b = b1

    def calP():
        return print(f"{calc.a+calc.b}")

    def calM():
        return print(f"{calc.a-calc.b}")
    
    def calC():
        return print(f"{calc.a*calc.b}")
    
    def calD():
        return print(f"{calc.a//calc.b}") # 몫 계산
    
    def calA():
        return print(f"{calc.a%calc.b}")
    
if __name__ == '__main__' :
    cal = calc
    a, b = map(int, input().split())
    cal.inp(a, b)
    cal.calP()
    cal.calM()
    cal.calC()
    cal.calD()
    cal.calA()

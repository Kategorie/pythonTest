def calc():
    in0 = int(input())
    in1 = int(input())
    
    ans01 = in1 % 100
    ans01 = in1 - ans01
    ans02 = in1 % 10
    ans02 = in1 - (ans01 + ans02)
    ans03 = in1 % 10

    a1 = in0 * ans03
    a2 = in0 * ans02
    a3 = in0 * ans01

    print(a1)
    print(int(a2 / 10))
    print(int(a3 / 100))

    print(a1 + a2 + a3)

if __name__ == '__main__':
    calc()
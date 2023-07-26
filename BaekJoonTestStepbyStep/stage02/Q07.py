if __name__ == '__main__':
    a,b,c = map(int, input().split())

    if a == b and b == c:
        price = 10000 + (a * 1000)
    elif a == b or b == c or a == c:
        if a == b or a == c:
            price = 1000 + (a * 100)
        elif b == c:
            price = 1000 + (b * 100)
    else:
        if b < a and c < a:
            price = a * 100
        elif b < c and a < c:
            price = c * 100
        elif c < b and a < b:
            price = b * 100
        else:
            print("err")

    print(price)


def quest(a,b,c):
    x = (a + b) % c
    y = (a * b) % c
    z = ( (a % c) + (b % c) ) % c
    r = ( (a % c) * (b % c) ) % c

    print(x)
    print(z)
    print(y)
    print(r)

if __name__ == '__main__' :
    a,b,c = map(int, input().split())
    quest(a,b,c)

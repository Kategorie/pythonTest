if __name__ == '__main__':
    while True:
        A,B = map(int, input().split())
        C = int(input())
        if A < 0 or 23 < A:
            print("input size error")
            continue
        elif B < 0 or 59 < B:
            print("input size error")
            continue
        elif C < 0 or 1000 < C:
            print("input size error")
            continue
        else:
            break

    B = B + C
    if 60 <= B:
        A = A + (B // 60)
        B = B % 60
    if 24 < A:
        A = A - 24
    if A == 24:
        A = 0
    
    print(A, B)
    


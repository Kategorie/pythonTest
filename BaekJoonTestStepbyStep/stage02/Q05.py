if __name__ == '__main__':
    while True:
        H,M = map(int, input().split())
        if H < 0 or 23 < H:
            continue
        elif M < 0 or 59 < M:
            continue
        else:
            if H == 0:
                H = 24
            break

    M = M - 45
    if M < 0:
        H = H - 1
        M = 60 - (-M)
    if H == 24:
        H = 0
    
    print(H, M)
    


if __name__ == '__main__' :
    while True:
        x = int(input())
        y = int(input())
        if x < -1000 or 1000 < x or x == 0:
            print("input size error")
            continue
        elif y < -1000 or 1000 < y or y == 0:
            print("input size error")
            continue
        else:
            break
    
    if 0 < x and 0 < y:
        print("1")
    elif x < 0 and 0 < y:
        print("2")
    elif x < 0 and y < 0:
        print("3")
    elif 0 < x and y < 0:
        print("4")
    else:
        print("err")
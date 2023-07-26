# Q.2-3

def func():
    while True:
        a = int(input())
        if 0 <= a & a <= 4000:
            break
    flag = 0
    if a % 4 == 0 and a % 100 != 0:
        flag = True
    elif a % 4 == 0 and a % 400 == 0:
        flag = True
    else:
        flag = False

    if  flag == 1 :
        print("1")
    elif flag == 0 :
        print("0")
    
func()
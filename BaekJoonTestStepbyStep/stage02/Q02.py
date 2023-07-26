# Q.2-2

def grade():
    while True:
        a = int(input())
        if 0 <= a & a <= 100:
            break
    
    if 89 < a:
        print("A")
    elif 79 < a & a < 90:
        print("B")
    elif 69 < a & a < 80:
        print("C")
    elif 59 < a & a < 70:
        print("D")
    else:
        print("F")

grade()
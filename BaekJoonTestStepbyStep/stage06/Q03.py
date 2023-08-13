a = int(input())
b = a
for k in range(a):
    b -= 1
    for i in range(b, 0, -1):
        print(" ", end="")
    for j in range(2*k+1):
        print("*", end="")
    print("")

for i in range(a-1,0,-1):
    b += 1
    for k in range(b):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print("")
    

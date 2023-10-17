N = int(input())
T = int(input())
W = int(input())
S = [N, T, W]
Sc = 0

if N == 60 and T == 60 and W == 60:
    print("Equilateral")
elif (N + T + W) == 180:
    for i in S:
        Sc = S.count(i)
    if Sc == 2:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")

S = []
tmp = []
Sc = 0
while True:
    tmp = list(map(int, input().split()))
    if tmp[0] == 0:
        break
    tmp.sort()
    S.append(tmp)

for j in range(len(S)):
    if S[j][2] < S[j][0] + S[j][1]:
        for i in S[j]:
            Sc = S[j].count(i)
            if Sc == 3:
                print("Equilateral")
                break
            elif Sc == 2:
                print("Isosceles")
                break
        if Sc == 1:
            print("Scalene")
    else:
        print("Invalid")

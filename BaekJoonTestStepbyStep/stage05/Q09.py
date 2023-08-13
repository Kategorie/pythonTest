AB = list(map(int,input().split()))
S = []
for j in range(len(AB)):
    a = AB[j] // 100
    b = (AB[j] // 10) % 10
    c = AB[j] % 10
    S.append((c*100)+(b*10)+a)
    

if S[0] < S[1]:
    print(S[1], end="")
else:
    print(S[0])

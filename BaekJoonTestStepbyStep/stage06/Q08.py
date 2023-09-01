res = 0
ans = 0
x = 0
S = []
G = {'A+' : 4.5, 'A0' : 4.0, 'B+' : 3.5, 'B0' : 3.0, 'C+' : 2.5, 'C0' : 2.0, 'D+' : 1.5, 'D0' : 1.0, 'F' : 0.0}

for i in range(20):
    S.append(input().split())
    if S[i-x][2] == 'P':
        S.pop()
        x += 1
    else:
        ans += (float(S[i-x][1]) * G[S[i-x][2]])
        res += float(S[i-x][1])

print(ans / res)
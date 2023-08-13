S = []
T = int(input())
for i in range(T):
    s = input()
    S.append(s)

for j in range(T):
    print(S[j][0],end="")
    print(S[j][-1])

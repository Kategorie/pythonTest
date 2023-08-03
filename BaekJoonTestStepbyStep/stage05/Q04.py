S = input()
J = 'abcdefghijklmnopqrstuvwxyz'
res = []

for jj in range(26):
    res.append(-1)
for i in range(len(S)):
    for j in range(len(J)):
        if S[i] == J[j]:
            if res[j] != -1:
                break
            res[j] = i

for ii in range(len(res)):
    print(res[ii], end=" ")
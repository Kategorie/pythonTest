D = {1:'1', 2:'ABC', 3:'DEF', 4:'GHI', 
     5:'JKL', 6:'MNO', 7:'PQRS', 8:'TUV', 9:'WXYZ', 0:'0'}
cnt = 0
S = list(input())
S.sort()
for i in range(len(D)):
    for j in range(len(S)):
        if D[i].count(S[j]):
            cnt += i+1

print(cnt)
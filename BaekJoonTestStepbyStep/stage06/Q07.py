N = int(input())    
L = []
cnt = 0
flag = False
for i in range(N):
    S = input()
    S += '*'
    if len(S) == 1:
        flag = True
    for ii in range(len(S)-1):
        if S[ii] != S[ii+1]:
            if ii == len(S) - 2:
                L.append(S[ii])
                L.append(S[ii+1])
            else:
                L.append(S[ii])
        elif len(S) > 1 and len(L) == 0:
            flag = True
    for iii in range(len(L)):
        if L.count(L[iii]) == 1:
            flag = True
        else:
            flag = False
            break
    if flag == True:
        cnt += 1
    #초기화
    L = []
    flag = False

print(cnt)
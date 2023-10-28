N = int(input())
cnt = 0
ans = []
inp = N
flag = False
if N % 3 == 0:
    ans.append(N // 3)
if N % 5 == 0:
    ans.append(N // 5)

while True:
    inp -= 3
    if 0 < inp:
        cnt += 1
        if inp % 5 == 0:
            ans.append(cnt + (inp // 5))
    elif inp == 0:
        break
    else:
        flag = True
        break
if flag and len(ans) == 0:
    print(-1)
else:
    ans.sort()
    print(ans[0])

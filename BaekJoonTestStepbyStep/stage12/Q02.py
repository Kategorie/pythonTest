N = input()
A = []
ans = []
for i in N:
    A.append(int(i))
tmp = []
for i in range(int(N)):
    inp = int(N) - i
    for j in str(inp):
        tmp.append(int(j))
    for k in range(len(tmp)):
        inp += tmp[k]
    if inp == int(N):
        ans.append(int(N) - i)
    inp = 0
    tmp = []

if 0 < len(ans):
    ans.sort()
    print(ans[0])
else:
    print(0)

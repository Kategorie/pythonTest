n = []
res = []
while True:
    a, b = map(int,input().split())
    n = [[a,b]]
    if  a == 0 and b == 0:
        break
    else:
        res.append(a+b)

for j in range(len(res)):
    print(res[j])
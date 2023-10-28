a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())
fn = 0
gn = 0
flag = False
for i in range(n0, 101):
    fn = a1 * i + a0
    gn = i
    if fn <= c * gn:
        flag = True
    else:
        flag = False
        break

if flag:
    print(1)
else:
    print(0)

N, B = input().split()
B = int(B) # 진법
N = int(N) # 문제 숫자

res = []
while True:
    a, b = divmod(N, B) # 몫, 나머지
    if b > 9:
        res.append(chr(b+55))
    else:
        res.append(chr(b+48))
    N = a
    if a == 0:
        break
    elif a < B:
        if a > 9:
            res.append(chr(a+55))
        else:
            res.append(chr(a+48))
        break
    
for iii in range(len(res)):        
    print(res[-(iii+1)], end="")
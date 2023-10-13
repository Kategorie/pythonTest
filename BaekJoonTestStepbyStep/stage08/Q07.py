# V = 높이, A = 올라가는 미터, B = 미끄러지는 미터
A, B, V = map(int, input().split())


ansA, ansB = divmod((V - B), (A - B))
if ansB == 0:
    print(ansA)
else:
    print(ansA+1)

'''
cnt += 1
if V <= 0:
    print(cnt)
'''

tmp = V - (A - B)
ans = tmp // B
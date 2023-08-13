S = list('abcdefghijklmnopqrstuvwxyz')
a = list(input().lower())
b = []

for k in range(len(S)):
    b.append(int(0))
for i in range(len(S)):
    for j in range(len(a)):
        if S[i] == a[j]:
            b[i] += 1

x = max(b)
if b.count(x) > 1:
    print("?")
else:
    print(S[b.index(x)].upper())
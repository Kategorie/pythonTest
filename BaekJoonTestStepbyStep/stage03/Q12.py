n = []
res = []

while True:
    try:
        a, b = map(int, input().split())
        n = [[a, b]]
        res.append(a + b)
    except:
        break

for j in range(len(res)):
    print(res[j])

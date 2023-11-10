N = []
for i in range(5):
    N.append(int(input()))

N.sort()
print(int((N[0] + N[1] + N[2] + N[3] + N[4]) / 5))
print(N[2])

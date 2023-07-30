while True:
    N = int(input())
    if 1000 < N or N < 4:
        continue
    else:
        break
for i in range(N//4):
    print("long ", end='')

print("int")
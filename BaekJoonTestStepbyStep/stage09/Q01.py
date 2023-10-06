A = []
B = []
while True:
    a,b = map(int, input().split())
    A.append(a)
    B.append(b)
    if a == 0 and b == 0:
        break

for i in range(len(A)-1):
    if A[i] < B[i] and B[i] // A[i] == 0:
        print('factor')
    elif B[i] < A[i] and A[i] // B [i] == 0:
        print('multiple')
    else:
        print('neither')
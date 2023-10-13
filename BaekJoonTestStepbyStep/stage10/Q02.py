A = list(map(int, input().split())) # x,y,w,h

if A[0] > A[2]-A[0]:
    ansA = A[2]-A[0]
else:
    ansA = A[0]
if A[1] > A[3]-A[1]:
    ansB = A[3]-A[1]
else:
    ansB = A[1]

if ansA < ansB:
    print(ansA)
else:
    print(ansB)
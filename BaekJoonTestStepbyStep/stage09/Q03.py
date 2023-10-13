n = 0
A = [] # 입력값
tmp = []
B = [] # 약수값
while True:
    n = int(input())
    if n == -1:
        break
    else: # 약수 구하는 코드
        A.append(n)
        for i in range(1, n):
            if n % i == 0:
                tmp.append(i)
            else:
                pass
    B.append(tmp)
    tmp = []

for k in range(len(A)):
    if A[k] == (sum(B[k])):
        print(A[k], "=", B[k][0], end="")
        for j in range(1, len(B[k])):
            print(" +", B[k][j], end="")
        print()
    else:
        print(A[k], "is NOT perfect.")
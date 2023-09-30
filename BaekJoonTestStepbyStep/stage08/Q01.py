'''
ord() # chr 2 ascii
chr() # ascii 2 chr
print(2 ** 10)  # 2의 10제곱
'''
N, B = input().split()
B = int(B)
N = list(N)
n = []

for i in N:
    if i.isdigit():
        n.append(int(ord(i)) - 48) # 48(0)-48
    elif i.isalpha():
        if i.islower():
            n.append(int(ord(i)) - 97) # 97(a)-97
        else: 
            n.append(int(ord(i)) - 55) # 65(A)-55

res = 0
for j in range(len(N)):
    res += n[-(j+1)] * (B ** j)
    print(f"n[-(j+1)] : {n[-(j+1)]}")
    print(f"B : {B}")
    print(f"j : {j}")
    print(f"res : {res}")
    
print(res)
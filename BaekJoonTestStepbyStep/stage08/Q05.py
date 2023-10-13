N = int(input())
layer = 1
for i in range(1, 200000000):
    layer += 6 * i
    
    if N == 1:
        print('1')
        break
    elif N <= layer:
        print(i +1)
        break
'''
# 6 12 18 24
# // 몫 % 나머지
N = int(input())

if N == 1:
    print("1")
else:
    print((((N**2)-1)//N)
'''
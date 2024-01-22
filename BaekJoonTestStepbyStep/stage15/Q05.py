def Eratos(data, num):
    prime = []
    num = num * num + 1
    for i in range(num):
        if i == 0 or i == 1:
            data[i] = False
        elif data[i] == True:
            prime.append(i)
            j = 2
            while i * j < num:
                data[i * j] = False
                j += 1
    return prime


N = int(input())
L = []
res = []
for _ in range(N):
    L.append(int(input()))

for i in range(N):  # n의 최대 약수가 sqrt(n) 이하
    flag = [True] * (L[i] * L[i] + 1)
    res.append(Eratos(flag, L[i]))


# 2중 리스트 플래그의 첫번째 True 인덱스를 출력하는 최악의 방법 ㅋㅋ
for x in range(N):
    for y in res[x]:
        if L[x] <= y:
            print(y)
            break


# 1. 소수는 무조건 제곱근 이하의 구간에 한개 이상 존재한다.
# 2. 현재 값을 기준으로 prime 값의 배수를 제거해 준다.
# 3. 1은 제외하고 2부터 배수를 찾는데 대신 2는 소수로 추가한다.
# 4. 주어진 값에서 가장 큰 수를 기준으로 한번 다 구한뒤 찾아서 하는 것과 매번 계산하는 것 중 뭐가 더 빠를지 고민해 봐야할듯
# 40억개 계산

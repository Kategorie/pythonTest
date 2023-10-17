X = int(input())
tmp = 1
a = 0
if X == 1:
    print("1/1")
else:
    while True:
        if X < tmp:  #
            tmp -= a
            a -= 1
            break
        else:
            tmp += a  # 현재 줄까지 더하기
            a += 1  # 몇번째 줄인지 카운트
    xx = X - (tmp)  # xx는 현재 탐색해야 하는 줄의 순서
    if a % 2 == 0:
        print(f"{xx}/{(a - (xx - 1))}")
    else:
        print(f"{(a - (xx - 1))}/{xx}")


"""
1 2  6 7

3 5 8

4 9

10
"""

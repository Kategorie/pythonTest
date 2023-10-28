"""
split을 사용한 다른 방법으로 시도해보기(split으로 입력을 바로 나눠버리기)
"""
N, M = map(int, input().split())
MN = []
c = ""
cnt = 0
ans = []
num = 8
flag = False
for i in range(N):
    MN.append(list(input()))

for j in range(N - (num - 1)):  # 세로
    for k in range(M - (num - 1)):  # 가로
        for y in range(2):
            for v in range(j, num + j):
                if y == 0:
                    if v % 2 == 0:
                        c = "W"
                    else:
                        c = "B"
                else:
                    if v % 2 == 0:
                        c = "B"
                    else:
                        c = "W"

                for x in range(k, num + k):
                    if c == "W":
                        if x % 2 == 1:
                            if MN[v][x] == "B":
                                flag = True  # 변경할 체스판이 없는 경우
                                # print("A", end="")
                                continue
                            else:
                                # print("B", end="")
                                flag = False
                                cnt += 1
                        elif x % 2 == 0:
                            if MN[v][x] == "B":
                                # print("C", end="")
                                flag = False
                                cnt += 1
                            else:
                                # print("D", end="")
                                flag = True
                                continue
                    elif c == "B":
                        if x % 2 == 1:
                            if MN[v][x] == "W":
                                # print("E", end="")
                                flag = True
                                continue
                            else:
                                # print("F", end="")
                                flag = False
                                cnt += 1
                        elif x % 2 == 0:
                            if MN[v][x] == "W":
                                flag = False
                                cnt += 1
                                # print("G", end="")
                            else:
                                # print("H", end="")
                                flag = True
                                continue
                # print()
            # print(cnt)
            # print("=======================================")

            flag = False
            ans.append(cnt)
            cnt = 0

if flag:
    print(0)
else:
    ans.sort()
    print(ans[0])

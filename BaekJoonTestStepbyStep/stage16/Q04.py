import sys

# [(()]).
param = ["(", ")", "[", "]"]
while True:
    data = sys.stdin.readline().split()
    stack = []
    # cnt = [0,0,0,0]
    if data[0] == ".":
        break
    else:
        for i in data:
            if i in param:
                stack.append(i)

        for j in stack:
            if j == "]":
                pass

        if cnt1 == 0 and cnt2 == 0:
            print("YES")
        else:
            print("NO")

"""
import sys

while True:
    data = list(sys.stdin.readline())
    if data[0] == ".":
        break
    else:
        cnt1 = 0
        cnt2 = 0
        for i in range(len(data)):
            if data[i] == "(" or data[i] == ")":
                if (
                    (64 < ord(data[i - 1]) and ord(data[i - 1]) < 91)
                    or (96 < ord(data[i - 1]) and ord(data[i - 1]) < 123)
                ) and (
                    (64 < ord(data[i + 1]) and ord(data[i + 1]) < 91)
                    or (96 < ord(data[i + 1]) and ord(data[i + 1]) < 123)
                ):
                    cnt1 = 1
                    break
                else:
                    if data[i] == "(":
                        cnt1 += 1
                    elif data[i] == ")" and cnt1 != 0:
                        cnt1 -= 1
                    elif data[i] == ")" and cnt1 == 0:
                        cnt1 = 1
                        break
            elif data[i] == "[" or data[i] == "]":
                if (
                    (64 < ord(data[i - 1]) and ord(data[i - 1]) < 91)
                    or (96 < ord(data[i - 1]) and ord(data[i - 1]) < 123)
                ) and (
                    (64 < ord(data[i + 1]) and ord(data[i + 1]) < 91)
                    or (96 < ord(data[i + 1]) and ord(data[i + 1]) < 123)
                ):
                    cnt2 = 1
                    break
                else:
                    if data[i] == "[":
                        cnt2 += 1
                    elif data[i] == "]" and cnt2 != 0:
                        cnt2 -= 1
                    elif data[i] == "]" and cnt2 == 0:
                        cnt2 = 1
                        break

        if cnt1 == 0 and cnt2 == 0:
            print("YES")
        else:
            print("NO")
"""

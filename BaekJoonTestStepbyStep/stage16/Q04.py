import sys

# [(()]).
param = ["(", ")", "[", "]"]
while True:
    data = str(input())  # sys.stdin.readline()
    stack = []
    # cnt = [0,0,0,0]
    if data[0] == ".":
        break
    else:
        for i in data:
            if i in param:
                stack.append(i)  # param 만 추출
        k = 0
        for j in range(len(stack)):
            if stack[0] in [")", "]"]:
                break
            elif (
                stack[(j - (k * 2))] == ")" and stack[((j - (k * 2))) - 1] == "("
            ) or (stack[(j - (k * 2))] == "]" and stack[((j - (k * 2))) - 1] == "["):
                stack.pop((j - (k * 2)))
                stack.pop(((j - (k * 2))) - 1)
                k += 1

        for j in stack:
            if j == "]":
                pass

        if cnt1 == 0 and cnt2 == 0:
            print("YES")
        if len(stack):
            print("no")
        else:
            print("yes")

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

# [(()]).
# (].
# )(.
# ([)].

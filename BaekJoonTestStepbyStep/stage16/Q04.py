import sys

param = ["(", ")", "[", "]"]
while True:
    data = str(input())  # sys.stdin.readline()
    stack = []
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

        if len(stack):
            print("no")
        else:
            print("yes")

# [(()]).
# (].
# )(.
# ([)].

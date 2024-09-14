import sys

N = int(sys.stdin.readline())

data = sys.stdin.readline().rstrip().split()
stack = []
num = 1
while num < N:
    j = 0
    i = 0
    for i in range(len(data) + len(stack)):
        if len(data) and data[i - j] == str(num):
            # print(data[i - j])  ##
            data.pop(i - j)
            j += 1
            num += 1
        elif len(stack) and stack[-1] == str(num):
            # print(stack[-1])  ##
            stack.pop(len(stack) - 1)
            j += 1
            num += 1
        elif len(stack) and len(data) == 0 and stack[-1] != str(num):
            print("Sad")
            sys.exit()  # 종료 시점의 예외처리를 주의할 것...
        else:
            stack.append(data[i - j])
            data.pop(i - j)
            j += 1

print("Nice")

# 5 4 1 3 2 Nice
# 5 1 3 2 4 Nice
# 4 1 3 2 5 Nice ##
# 5 4 3 2 1 10 9 8 7 6 Nice
# 2 1 4 3 5 Nice
# 2 1 5 4 3 Nice
# 4 2 1 3 Nice
# 2 3 1 5 6 7 10 9 8 4 Sad
# 3 12 5 6 1 4 2 7 15 19 16 20 13 8 17 9 10 18 11 14 Sad

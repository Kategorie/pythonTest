def stack_in(data, num):
    data.append(num)


def stack_out(data, print_except):
    if print_except:
        for i in range(1, len(data)):
            print(data[i])
    else:
        print(data[0])


def stack_check(data, print_flag):
    flag = False
    if len(data):
        flag = True
        if print_flag:
            stack_out(data, False)
    else:
        flag = False

    return flag


def execute():
    data = []

    M = int(input())
    for i in range(M):
        order = list(map(int, input().split()))

        if order[0] == 1:
            stack_in(data, order[1])
        elif order[0] == 2:
            stack_out(data, True)
        elif order[0] == 3:
            print(len(data))
        elif order[0] == 4:
            if stack_check(data, False):
                print("0")
            else:
                print("1")
        elif order[0] == 5:
            if stack_check(data, False):
                stack_check(data, True)
            else:
                print("-1")
        else:
            pass


execute()

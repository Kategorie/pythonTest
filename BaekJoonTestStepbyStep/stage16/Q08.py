N, K = map(int, input().split())
cnt = 1
queue = [x for x in range(1, N + 1)]
res_stack = []
while len(res_stack) != N:
    for i in range(len(queue)):
        if queue[i] == 0:
            pass
        else:
            if cnt % K == 0:
                res_stack.append(queue[i])
                queue[i] = 0
            cnt += 1

res = "<"
for x in range(len(res_stack) - 1):
    res += str(res_stack[x]) + ", "
res = res + str(res_stack[-1]) + ">"
print(res)

"""
알고리즘
스택 두개로
반복 조건 1 결과 스택 개수가 초기 개수가 되면 종료
반복 조건 2 입력 스택 한번 다 돌면 종료
카운터 1 반복 밖에서 초기화, 반복조건 2에서 무조건 ++, k 나머지가 0일때 결과 스택에 추가 후 입력스택 윛 0으로 변경
반복조건 2에서 입력스택 값이 0이면 pass
"""

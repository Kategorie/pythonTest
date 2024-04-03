import sys

N = int(input())

inp_q = list(map(int, sys.stdin.readline().split()))
chk_inp = [x for x in range(1, N + 1)]

cnt = inp_q.pop(0)
print("1", end=" ")
idx = 0
res = 0
for _ in range(N - 1):
    if len(inp_q):
        if cnt < 0:
            tmp = idx + cnt
            if len(inp_q) <= abs(tmp):
                while True:
                    tmp = -(abs(tmp) - len(inp_q))
                    if abs(tmp) < len(inp_q):
                        break
                idx = inp_q.index(inp_q[tmp])
                cnt = inp_q.pop(tmp)
            else:
                idx = inp_q.index(inp_q[tmp])
                cnt = inp_q.pop(tmp)
            res = idx + cnt
        else:
            idx = cnt - 1
            if len(inp_q) <= abs(idx):
                while True:
                    idx = idx - len(inp_q)
                    if abs(idx) < len(inp_q):
                        break
                cnt = inp_q.pop(idx)
            else:
                cnt = inp_q.pop(idx)
            res = idx
        print(res + 1, end=" ")
    else:
        break

"""
1번



zip [][] list
"""

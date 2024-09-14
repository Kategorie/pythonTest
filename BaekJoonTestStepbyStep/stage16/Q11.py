"""
# 예술이네
import sys

N = sys.stdin.readline()
A = sys.stdin.readline().split()
B = [b for a, b in zip(A, sys.stdin.readline().split()) if a == "0"][::-1] # 리스트 꿀팁
M = int(sys.stdin.readline())
B.extend(sys.stdin.readline().split())
print(" ".join(B[:M]))
"""

import sys
from collections import deque

N = int(input())
qstack_flag = sys.stdin.readline().rstrip().split()
inp_data = sys.stdin.readline().rstrip().split()
M = int(input())
inp_ary = sys.stdin.readline().rstrip().split()

res_q = deque()
for i in range(N):
    if qstack_flag[i] == "0":
        res_q.appendleft(inp_data[i])
    else:
        pass

for j in range(M):
    res_q.append(inp_ary[j])
    print(res_q[j], end=" ")

"""
양동이 4개 중 0인 양동이에 물을 부으면 넘쳐서 옆의 0번 양동이로 가고 결국 마지막 0번 양동이 물이 넘쳐서 출력되는걸 생각하면 된다.
들어가는 양동이가 3개면 나오는 양동이는 끝에서 3개까지인 셈.
"""

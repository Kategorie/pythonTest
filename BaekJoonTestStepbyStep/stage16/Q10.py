import sys
from collections import deque

N = int(input())
inp_q = deque(list(map(int, sys.stdin.readline().split())))
idx_q = deque([x for x in range(2, N + 1)])

print("1", end=" ")
now_data = inp_q.popleft()
while len(inp_q):
    if 0 < now_data:
        now_data = now_data - 1
    inp_q.rotate(-now_data)
    idx_q.rotate(-now_data)
    now_data = inp_q.popleft()
    idx = idx_q.popleft()
    print(idx, end=" ")


# rotate()
# enumerate()

# 1 5 3 2 4


"""
 1  2  3  4  5
-5 -5 -5 -5 -5

 2  3  4  5		 1
-5 -5 -5 -5		-5

 5  2  3  4		 1
-5 -5 -5 -5		-5

 2  3  4		 5
-5 -5 -5		-5

 3  4  2		 5
-5 -5 -5		-5

 4  2			 3
-5 -5			-5

 2  4			 3
-5 -5			-5

 4			 2	 
-5			-5



 1  2  3  4  5
 3  2  1 -3 -1

 2  3  4  5		 1
 2  1 -3 -1		 3

 4  5  2  3 		 1
-3 -1	2  1 		 3

 5  2  3 		 4
-1  2  1		-3

 5  2  3 		 4
-1  2  1		-3

 3  2 			 5
 1  2			-1

2			3
2			1

"""

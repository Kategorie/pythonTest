import sys
from collections import deque
import time

time_start = time.time()


N = int(input())

queue = deque(x for x in range(1, N + 1))

while len(queue) != 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])

time_end = time.time()
time_result = time_end - time_start
print(str(time_result))

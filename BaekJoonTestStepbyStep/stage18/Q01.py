import sys

A = int(input())
data = list(map(int, sys.stdin.readline().split()))

data.sort()

print(data[0] * data[-1])

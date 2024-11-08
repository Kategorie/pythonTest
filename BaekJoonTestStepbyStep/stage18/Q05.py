import sys
import collections

"""
N, M = map(int, sys.stdin.readline().split())
data = []
for _ in range(N):
    input_ = sys.stdin.readline().rstrip()
    if M <= len(input_):
        data.append(input_)
"""
N = 12
M = 4
data = [
    "abbbb",
    "abbbb",
    "abbbb",
    "acccc",
    "acccc",
    "acccc",
    "aaaaa",
    "aaaaa",
    "aaaaa",
    "adddd",
    "adddd",
    "adddd",
]

res = []
data_c = collections.Counter(data)
s_data_c = sorted(data_c.items(), key=lambda x: x[1], reverse=True)
tmp = []
for i in range(1, len(s_data_c)):
    if s_data_c[i - 1][1] == s_data_c[i][1]:  # 빈도 수가 같을 때,
        tmp.append(s_data_c[i - 1][0])
    else:  # 빈도 수가 다를 때,
        if tmp:  # 빈도 수가 같은 경우의 리스트를 문자열 길이로 정렬
            tmp.append(s_data_c[i - 1][0])
            tmp = sorted(tmp, key=len, reverse=True)
            res += tmp
            tmp = []
        else:
            res.append(s_data_c[i - 1][0])

if tmp:  # 빈도 수가 같은 경우로 반복이 종료될 경우,
    tmp.append(s_data_c[i][0])  # 마지막 요소 추가
    tmp = sorted(tmp, key=len, reverse=True)
    res += tmp
    tmp = []
else:  # 빈도 수가 다른 경우로 반복이 종료될 경우,
    res.append(s_data_c[i][0])  # 마지막 요소 추가

for r in res:
    print(r)

"""
N = 12
M = 5
data = [
    "appearance",
    "append",
    "attendance",
    "swim",
    "swift",
    "swift",
    "swift",
    "mouse",
    "wallet",
    "mouse",
    "ice",
    "age",
]
"""
"""
N = 7
M = 4
data = [
    "apple",
    "ant",
    "sand",
    "apple",
    "append",
    "sand",
    "sand",
]
"""
"""
N = 9
M = 4
data = [
    "apple",
    "attend",
    "list",
    "attend",
    "attend",
    "apple",
    "apple",
    "create",
    "garage",
]
"""

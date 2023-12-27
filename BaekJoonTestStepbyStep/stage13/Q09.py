def sorting(arr, B, num):
    tmp = []
    for k in range(1, num + 1):
        for i in arr:
            if len(i) == k:  # 단어 길이가 같은 것끼리 리스트로 묶음
                tmp.append(i)
        if 1 < len(tmp):
            tmp.sort()  # 단어 길이가 같은걸 정렬해서 새 리스트에 추가
        for j in tmp:
            B.append(j)
        tmp = []
    return B


if __name__ == "__main__":
    N = 5  # int(input())
    A = ["c", "b", "b", "b", "c"]
    tmp = []
    B = []
    # "but","i","wont","hesitate","no","more","no","more","it","cannot","wait","im","yours"
    # for _ in range(N):
    #    A.append(input())

    for i in A:  # 같은 단어 제거
        tmp.append(i)
        if tmp.count(i) == 1:
            pass
        else:
            tmp.remove(i)

    B = sorting(tmp, B, 50)  # p3 : 각 문자열의 길이

    for j in B:
        print(j)

########################################################################
# set 메서드를 사용해서 풀 수도 있음 (참고)
"""
N = int(input())
arr = [[] for _ in range(51)]
for _ in range(N):
    a = input()
    arr[len(a)].append(a)

for i in arr:
    if len(i) == 0:
        pass
    else:
        temp = sorted(list(set(i)))  # i = list
        for j in temp:
            print(j)
"""

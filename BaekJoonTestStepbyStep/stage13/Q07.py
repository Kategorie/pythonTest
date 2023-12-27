N = int(input())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))
A.sort()
for i in A:
    for j in i:
        print(j, end=" ")
    print()
"""
# 망할 시간 초과
import time


def shiftDown(arr, parentIdx, size, flag):
    leftIdx = 2 * parentIdx + 1
    rightIdx = leftIdx + 1
    largestIdx = -1

    if leftIdx < size:
        largestIdx = leftIdx

    if rightIdx < size and arr[leftIdx][flag] < arr[rightIdx][flag]:
        largestIdx = rightIdx

    if largestIdx != -1 and arr[parentIdx][flag] < arr[largestIdx][flag]:
        tmp = arr[parentIdx]
        arr[parentIdx] = arr[largestIdx]
        arr[largestIdx] = tmp
        shiftDown(arr, largestIdx, size, flag)


def heapSort(arr, size, flag):
    for i in range(int(size / 2), -1, -1):  # parentIdx
        shiftDown(arr, i, size, flag)
    if flag:
        for j in range(size - 1, 0, -1):
            tmp = arr[0]
            arr[0] = arr[j]
            arr[j] = tmp
            shiftDown(arr, 0, j, flag)
    else:
        tmp_idx = 0
        f = True
        j = size - 1
        tmp_arr = []
        while 0 < j:
            if f:
                tmp = arr[0]
                arr[0] = arr[j]
                arr[j] = tmp
                tmp_arr.append(arr[j])
                tmp_idx = j
            L = len(tmp_arr)
            if (1 < L and tmp_arr[L - 1][0] != tmp_arr[L - 2][0]) or f != True:
                if f:
                    tmp_arr.pop()
                    tmp_idx += 1
                L = len(tmp_arr)
                if 1 < L:
                    heapSort(tmp_arr, L, 1)
                    for k in range(L):
                        arr[tmp_idx + k] = tmp_arr[k]
                    tmp_arr = []
                    tmp_arr.append(arr[j])
                else:
                    tmp_arr = []
                    tmp_arr.append(arr[j])

            if j == 1 and f:
                tmp_arr.append(arr[j - 1])
                j += 1
                tmp_idx = 0
                f = False
            if f:
                shiftDown(arr, 0, j, flag)
            j -= 1


if __name__ == "__main__":
    start = time.time()
    N = 8  # int(input())
    # [[1, 1], [1, -1], [1, 5], [1, -3]]
    A = [
        [3, 2],
        [3, 4],
        [1, 1],
        [1, -1],
        [2, 2],
        [3, 3],
        [0, 2],
        [0, 1],
        [0, 0],
        [1, -3],
    ]
    # for _ in range(N):
    #    A.append(list(map(int, input().split())))

    heapSort(A, len(A), 0)  # 0 : x를 기준으로 정렬, 1 : y를 기준으로 정렬
    for i in A:
        for j in i:
            print(j, end=" ")
        print()
    end = time.time()
    print(f"{end - start:.5f} sec")
"""
"""
import sys

input = sys.stdin.readline


def shiftDown(arr, parentIdx, size, flag):
    leftIdx = 2 * parentIdx + 1
    rightIdx = leftIdx + 1
    largestIdx = -1

    if leftIdx < size:
        largestIdx = leftIdx

    if rightIdx < size and arr[leftIdx][flag] < arr[rightIdx][flag]:
        largestIdx = rightIdx

    if largestIdx != -1 and arr[parentIdx][flag] < arr[largestIdx][flag]:
        tmp = arr[parentIdx]
        arr[parentIdx] = arr[largestIdx]
        arr[largestIdx] = tmp
        shiftDown(arr, largestIdx, size, flag)


def heapSort(arr, size, flag):
    for i in range(int(size / 2), -1, -1):  # parentIdx
        shiftDown(arr, i, size, flag)
    if flag:
        for j in range(size - 1, 0, -1):
            tmp = arr[0]
            arr[0] = arr[j]
            arr[j] = tmp
            shiftDown(arr, 0, j, flag)
    else:
        tmp_idx = 0
        f = True
        j = size - 1
        tmp_arr = []
        while 0 < j:
            if f:
                tmp = arr[0]
                arr[0] = arr[j]
                arr[j] = tmp
                tmp_arr.append(arr[j])
                tmp_idx = j
            L = len(tmp_arr)
            if (1 < L and tmp_arr[L - 1][0] != tmp_arr[L - 2][0]) or f != True:
                if f:
                    tmp_arr.pop()
                    tmp_idx += 1
                L = len(tmp_arr)
                if 1 < L:
                    heapSort(tmp_arr, L, 1)
                    for k in range(L):
                        arr[tmp_idx + k] = tmp_arr[k]
                    tmp_arr = []
                    tmp_arr.append(arr[j])
                else:
                    tmp_arr = []
                    tmp_arr.append(arr[j])

            if j == 1 and f:
                tmp_arr.append(arr[j - 1])
                j += 1
                tmp_idx = 0
                f = False
            if f:
                shiftDown(arr, 0, j, flag)
            j -= 1


if __name__ == "__main__":
    N = int(input().rstrip())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().rstrip().split())))

    heapSort(A, len(A), 0)  # 0 : x를 기준으로 정렬, 1 : y를 기준으로 정렬
    for i in A:
        for j in i:
            print(j, end=" ")
        print()
"""

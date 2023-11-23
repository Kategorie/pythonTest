def shiftDown(arr, parentIdx, size):
    leftIdx = parentIdx * 2 + 1
    rightIdx = leftIdx + 1
    # 자식 노드 중 더 큰 값. 재귀 함수에서 말단 노드가 존재할 경우를 대비해 예외처리
    largeIdx = -1

    # 현재 노드(부모노드)에서 왼쪽 자식노드만 있는 경우.
    if leftIdx < size:
        largeIdx = leftIdx

    # 현재 노드(부모노드)에서 오른쪽 자식노드도 있는 경우.
    if rightIdx < size and arr[leftIdx] < arr[rightIdx]:
        largeIdx = rightIdx  # 오른쪽 자식 노드가 더 큰 경우.

    if largeIdx != -1 and arr[parentIdx] < arr[largeIdx]:
        tmp = arr[largeIdx]
        arr[largeIdx] = arr[parentIdx]
        arr[parentIdx] = tmp
        shiftDown(arr, largeIdx, size)  # 노드 변경 후 하위 트리 구조가 모두 재정렬 될 수 있도록 재귀함수 호출


def heapSort(arr, size):
    # 배열을 최대 힙으로 변경 -> heapify
    for i in range(int(size / 2), -1, -1):  # parentIdx
        shiftDown(arr, i, size)

    # 최대 힙에서 루트를 제외한 나머지에 대해 정렬
    # 정렬 후 루트값을 매번 제외하고 나머지들에 대해 다시 정렬
    for i in range(size - 1, 0, -1):
        tmp = arr[0]
        arr[0] = arr[i]
        arr[i] = tmp
        shiftDown(arr, 0, i)


if __name__ == "__main__":
    N = list(input())

    N = list(map(int, N))

    heapSort(N, len(N))
    for i in range(len(N) - 1, -1, -1):
        print(N[i], end="")

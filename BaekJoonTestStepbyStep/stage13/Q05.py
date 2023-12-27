# 8MB 메모리 제한
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input().rstrip())
    max_eliment = 10000
    counting_arr = [0] * (max_eliment + 1)
    for i in range(N):
        input_tmp = int(input().rstrip())
        # 각 요소의 개수를 의미하는 배열 생성
        # ex/counting_arr의 3번째 원소가 2일때, 정렬 전 배열에 3이 2개 있다는 의미
        counting_arr[input_tmp] += 1

        # 즉, 이미 counting_arr의 인덱스를 이용해 정렬이 되어 있으므로 이걸 그대로 개수만 반복해서 출력해주면 된다.
        # 미친 천재다
    for i in range(max_eliment + 1):
        # 이미 정렬되어 있으니 요소가 0인 경우 해당 요소는 없다는 의미이다.
        if counting_arr[i] != 0:
            for j in range(counting_arr[i]):  # 정렬된 요소를 몇번 출력해야 되는지
                print(i)
"""
import sys  # 빠른 입출력을 위한 라이브러리

# 빠른 입출력을 위한 오버로드
input = sys.stdin.readline
print = sys.stdout.write


def counting(arr):
    max_eliment = max(arr)  # 정렬 전 배열 중 최대값
    # 카운팅 하려면 원소 중 제일 큰 값보다 큰 배열이 있어야함
    counting_arr = [0] * (max_eliment + 1)

    for a in arr:
        # 입력 배열의 요소를 인덱스로 갖는 c 배열 생성하고
        # 같은 숫자 나올 때마다 1씩 추가
        counting_arr[a] += 1

    for i in range(1, max_eliment + 1):  # 0번은 첫번째니까 누적할게 없음
        # 누적합 배열로 변경 (현재 인덱스의 값 = 현재 값 + 직전 인덱스 값)
        counting_arr[i] += counting_arr[i - 1]
        # 누적합 배열의 각 원소(ex/int=3)의 의미는 현 인덱스(ex/idx=3)에서
        # 원소 값만큼의 범위(ex/idx=1~3)에 해당 원소(ex/int=3)가 포함되어 있다는 의미이다.

    # 정렬될 결과 배열
    result = [0] * len(arr)

    for a in arr:
        # 누접합 배열의 값을 결과 인덱스로 하고, 해당 인덱스의 누적합 배열의 인덱스를 추가한다.
        result[counting_arr[a] - 1] = a
        # 누적합 배열에서 하나를 썼으니 하나를 빼준다.
        counting_arr[a] -= 1

    return result


if __name__ == "__main__":
    N = 10  # int(input().rstrip())
    n = [10, 2, 4, 5, 3, 5, 2, 6, 1, 2]
    # for i in range(N):
    #    n.append(int(input().rstrip()))
    a = counting(n)
    for j in range(N):
        print(str(a[j]) + "\n")
"""

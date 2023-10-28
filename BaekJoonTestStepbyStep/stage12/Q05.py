# count 함수 사용법 주의 (반례 : 결과값이 666666이 될 때 조심할 것)
N = int(input())
cnt = 1
end = 666

while True:
    if cnt == N:
        print(end)
        break
    end += 1
    if str(end).count("666"):
        cnt += 1

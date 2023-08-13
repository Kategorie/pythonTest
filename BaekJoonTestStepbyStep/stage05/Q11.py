#종결규칙이 없으면 EOF try-ecept로 해결

while True:
    try:
        S = input()
        print(S)
    except:
        break
T = int(input())
for tc in range(1, T+1):
    txt = input()

    total = 0
    for j in range(len(txt) // 2):
        if txt[j] != txt[len(txt) - 1 - j]:
            total = 0
        else:
            total = 1


    print(f"#{tc} {total}")
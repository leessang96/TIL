T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    max_v = 0
    for i in range(len(str1)):
        total = 0
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                total += 1

        if max_v < total:
            max_v = total

    print(f"#{tc} {max_v}")

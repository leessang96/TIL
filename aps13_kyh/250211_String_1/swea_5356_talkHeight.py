T = int(input())
for tc in range(1, T+1):
    s_list = []
    for _ in range(5):
        str1 = input()
        s_list.append(str1)

    max_l = 0
    for i in range(len(s_list)):
        if max_l < len(s_list[i]):
            max_l = len(s_list[i])

    for i in range(len(s_list)):
        if len(s_list[i]) < max_l:
            s_list[i] += ' ' * (max_l - len(s_list[i]))

    print(f"#{tc}", end=' ')
    for i in range(max_l):
        for j in range(5):
            if s_list[j][i] == ' ':
                continue
            else:
                print(s_list[j][i], end='')
    print()
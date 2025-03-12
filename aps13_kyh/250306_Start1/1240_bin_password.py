T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    pass_code_dict = {'0001101': 0, '0011001' : 1, '0010011' : 2, '0111101' : 3, '0100011' : 4,
                      '0110001': 5, '0101111' : 6, '0111011' : 7, '0110111' : 8, '0001011' : 9}

    i, j = N-1, M-1
    while True:
        if j <= -1:
            j = M-1
            i -= 1

        if arr[i][j] == '1':
            si, sj = i, j
            pass_list = arr[si][sj-55: sj+1]
            break
        else:
            j -= 1

    idx = 0
    pass_code_list = []
    for k in range(7, len(pass_list)+1, 7):
        pass_code_list.append(pass_list[idx:k])
        idx += 7

    bin_code = []
    for i in range(len(pass_code_list)):
        code_str = ''
        for j in pass_code_list[i]:
            code_str += j

        bin_code.append(code_str)

    s1 = 0
    s2 = 0
    i = 1
    while bin_code:
        if i % 2 != 0:
            s1 += pass_code_dict[bin_code.pop(0)]
        else:
            s2 += pass_code_dict[bin_code.pop(0)]

        i += 1

    s = (s1 * 3) + s2
    if s % 10 == 0:
        print(f"#{tc} {s1 + s2}")
    else:
        print(f"#{tc} 0")
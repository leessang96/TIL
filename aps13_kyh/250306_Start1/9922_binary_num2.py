T = int(input())
for tc in range(1, T+1):
    N = float(input())

    bin_num = ''
    i = 1

    for i in range(1, 14):
        if N == 0:
            break
        elif N - (2 ** (-i)) >= 0:
            bin_num += '1'
            N = N - (2 ** (-i))
        else:
            bin_num += '0'

    if len(bin_num) >= 13:
        print(f"#{tc} overflow")
    else:
        print(f"#{tc} {bin_num}")



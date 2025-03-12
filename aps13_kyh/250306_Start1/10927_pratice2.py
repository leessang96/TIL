T = int(input())
for tc in range(1, T+1):
    N = int(input())
    hex_str = input()

    # 0123456789ABCDEF"
    hex_bin = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
               '4': '0100', '5': '0101', '6': '0110', '7': '0111',
               '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
               'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

    bin_num = ''
    for i in hex_str:
        bin_num += hex_bin[i]

    bin_str_list = []
    idx = 0
    for j in range(7, len(bin_num)+1, 7):
        bin_str_list.append(bin_num[idx:j])
        idx += 7

    bin_list = []
    for k in bin_str_list:
        s = 0
        i = 1  # 지수
        bin_k = int(k)
        while bin_k > 0:
            num = bin_k % 10        # 뒤에서부터 한자리 씩
            s += (num) * (2 ** i)
            i += 1
            bin_k //= 10

        s //= 2
        bin_list.append(s)

    print(f"#{tc}", *bin_list)
T = int(input())
for tc in range(1, T+1):
    n, arr = input().split()

    # 0123456789ABCDEF"
    hex_bin = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
               '4': '0100', '5': '0101', '6': '0110', '7': '0111',
               '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
               'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

    binary_list = []
    for i in arr:
        binary_list.append(hex_bin[i])

    print(f"#{tc}", end=' ')
    for i in binary_list:
        print(i, end='')
    print()

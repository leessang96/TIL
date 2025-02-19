T = int(input())
for tc in range(1, T+1):
    tc_num, N = input().split()
    arr_num = input().split()
    count_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    count_dict = {"ZRO": 0, "ONE": 0, "TWO": 0, "THR": 0, "FOR": 0, "FIV": 0, "SIX": 0, "SVN": 0, "EGT": 0, "NIN": 0}
    for i in range(int(N)):
        count_dict[arr_num[i]] += 1

    print(count_dict)
    print(f'{tc_num} ', end='')

    for num in count_list:
        for _ in range(count_dict[num]):
            print(num, end=' ')

    print()
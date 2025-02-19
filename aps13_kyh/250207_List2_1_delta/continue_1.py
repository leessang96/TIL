'''
3
10
0011001110
10
0000100001
10
0111001111

'''
T = int(input())
for tc in range(1, T + 1):
    N = int(input())                        # 수열의 길이 N
    prob_series = list(map(int, input()))    # 수열을 받아서 list로
    # print(prob_series)

    continue_list = [0] * 1000    # 연속된 숫자의 개수를 저장할 리스트 생성
    # T의 최댓값인 1000으로 생성해서, append를 하지 않게 만들었음.
    count_continue = 0  # 얼마나 연속되는지 셀 변수
    max_value = 0

    for idx, i in enumerate(prob_series):
        # print('idx, i =', idx, i)
        if i == 1:
            count_continue += 1
            continue_list[idx] = count_continue
        if i == 0:
            count_continue = 0
            continue_list[idx] = count_continue

    for i in continue_list:
        if max_value < i:
            max_value = i

    # print(continue_list)
    # print(max_value)
    print(f'#{tc} {max_value}')
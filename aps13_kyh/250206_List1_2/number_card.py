# 오늘 배운 정렬 + 어제 min max
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    number_list = list(map(int, input()))
    # print(number_list)

    a_i = 10            # 숫자 a_i는 최대 9
    COUNTS = [0] * a_i

    for i in number_list:
        COUNTS[i] += 1
    # print(COUNTS)

    # COUNTS 리스트에서 바로 최대 카운트 비교
    max_count = 0
    max_number = 0
    for idx, i in enumerate(COUNTS):
        if i >= max_count:
            max_count = i
            max_number = idx
    # print(max_number, max_count)
    print(f'#{tc} {max_number} {max_count}')

    # for i in range(1, a_i):
    #     COUNTS[i] += COUNTS[i - 1]  # 누적합으로 COUNTS list 변경
    # print(COUNTS)

    # 이건 그냥 counting sort 구현
    # sorted_list = [0] * len(number_list)        # 정 렬된 결과를 넣을 리스트
    # for i in range(len(number_list) - 1, -1, -1):
    #     # print(i)
    #     COUNTS[number_list[i]] -= 1
    #     # print(COUNTS)
    #     sorted_list[COUNTS[number_list[i]]] = number_list[i]
    # print(sorted_list)

    # for i in range(1, len(number_list)):
    #     diff = COUNTS[i] - COUNTS[i - 1]






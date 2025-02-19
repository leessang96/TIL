T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    # print(arr)
    min_value = 11      # a_i의 최댓값은 10
    max_value = 0       # a_i의 최솟값은 1

    min_position = 0
    max_position = 0
    idx = 0
    for i in arr:
        # print(min_value, min_position, max_value, max_position)
        # print()

        if min_value > i:
            # print(min_value, min_position, max_value, max_position)
            min_value = i
            min_position = idx
            idx += 1
            continue
            # print(min_value, min_position, max_value, max_position)
            # print()

        if max_value <= i:
            # print(min_value, min_position, max_value, max_position)
            max_value = i
            max_position = idx
            idx += 1
            continue
            # print(min_value, min_position, max_value, max_position)
            # print()

        else:
            # print(min_value, min_position, max_value, max_position)
            idx += 1
            # print(min_value, min_position, max_value, max_position)
            # print()

    # print(max_value, max_position)
    # print(min_value, min_position)
    # print()
    # print()

    # 내장함수 abs 쓰는 경우
    # result = abs(max_position - min_position)

    # 내장함수 abs 안쓰는 경우
    result = max_position - min_position

    if max_position < min_position:
        result = min_position - max_position

    print(f'#{tc} {result}')

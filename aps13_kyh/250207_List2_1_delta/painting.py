'''
3
2
2 2 4 4 1
3 3 6 6 2
3
1 2 3 3 1
3 6 6 8 1
2 3 5 6 2
3
1 4 8 5 1
1 8 3 9 1
3 2 5 8 2

'''
T = int(input())
for tc in range(1, T + 1):
    # 기본 바탕을 0으로 한 후, red / blue에 따라 해당 위치에
    # 숫자를 더할 것. 그럼 색칠된 부분 구분이 됨.
    plate = [[0] * 10 for _ in range(10)]

    # 만약 같은 색이 겹칠 수 있다면
    # 영역의 개수 N <= 30 이므로,
    # 두 color의 구분은 100의 자릿수와 1의 자릿수로 하는게 안겹침
    # ex - 129 -> 100 한 번, 1 29번으로 확실히 구분 가능
    # red -> +100, blue -> +1로 지정

    # but 현재는 문제 조건에 같은 색 안겹친다는 조건 o
    # -> 그냥 red / blue 모드 +1로 지정하여 풀 것.
    N = int(input())
    # print(N)
    for _ in range(N):
        left_top_i, left_top_j, right_bot_i, right_bot_j, color = list(map(int, input().split()))
        # print(left_top_i, left_top_j, right_bot_i, right_bot_j, color)
        count = 0       # 겹친 부분의 수를 찾을 변수
        for i in range(left_top_i, right_bot_i + 1):
            #
            for j in range(left_top_j, right_bot_j + 1):
                plate[i][j] += 1
    for i in range(len(plate)):     # 도화지 크기 10 x 10
        # maxrix: rectangular shape 이기에,아무 요소나 찍어도 열의 수는 같음
        # -> plate[0]
        for j in range(len(plate[0])):
            if plate[i][j] == 2:
                count += 1
        # print(plate)
    print(f'#{tc} {count}')




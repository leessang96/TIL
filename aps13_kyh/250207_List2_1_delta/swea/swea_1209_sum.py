T = 10
for tc in range(1, T+1):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_v = 0
    s = 0
    # 행
    for i in range(100):
        s1 = 0
        for j in range(100):
            s1 += arr[i][j]

        if max_v < s1:
            max_v = s1

    # 열
    for i in range(100):
        s2 = 0
        for j in range(100):
            s2 += arr[j][i]

        if max_v < s2:
            max_v = s2

    # 대각 ->
    s3 = 0
    for i in range(100):
        s3 += arr[i][i]

    if max_v < s3:
        max_v = s3

    # 대각 <-
    s4 = 0
    for i in range(100):
        s4 += arr[i][100 - i - 1]

    if max_v < s4:
        max_v = s4

    print(f'#{t} {max_v}')
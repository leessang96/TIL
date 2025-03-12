for tc in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_v = 0

    for i in range(100):
        s = 0
        for j in range(100):
            s += arr[i][j]
        if max_v < s:
            max_v = s

    for i in range(100):
        s = 0
        for j in range(100):
            s += arr[j][i]
        if max_v < s:
            max_v = s

    s = 0
    for i in range(100):
        s += arr[i][i]
    if max_v < s:
        max_v = s


    print(f"#{tc} {max_v}")


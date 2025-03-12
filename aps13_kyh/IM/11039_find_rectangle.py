T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_v = 0
    for i in range(n):
        for j in range(n):
            w = 0
            h = 0
            if arr[i][j] == 1:
                for k in range(i, n):
                    if arr[k][j] == 1:
                        h += 1
                    else:
                        break

                for l in range(j, n):
                    if arr[i][l] == 1:
                        w += 1
                    else:
                        break

            if max_v < w * h:
                max_v = w * h

    print(f"#{tc} {max_v}")

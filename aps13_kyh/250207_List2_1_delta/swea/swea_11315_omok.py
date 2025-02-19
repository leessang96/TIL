T = 1
for tc in range(1, T+1):
    n = int(input())
    arr = [input() for _ in range(n)]

    flag = False

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'o':
                for k in range(1, 5):
                    c = 1
                    for di, dj in [[0,1], [1,0], [1,1], [-1,-1]]:
                        ni = i + di * k
                        nj = j + dj * k

                        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 'o':
                            c += 1
                    if c == 5:
                        flag = True
                        break

    if flag:
        print(f"#{tc} YES")
    else:
        print(f"#{tc} NO")

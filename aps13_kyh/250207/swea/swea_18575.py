T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_v = 0
    min_v = 100000
    for i in range(n):
        for j in range(n):
            s = arr[i][j]
            for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
                for c in range(1, n):
                    ni = i + di * c
                    nj = j + dj * c

                    if 0 <= ni < n and 0 <= nj < n:
                        s += arr[ni][nj]
            if max_v < s:
                max_v = s
            if min_v > s:
                min_v = s

    print(f"#{tc} {max_v - min_v}")
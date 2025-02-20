# T = int(input())
# for tc in range(1, T+1):
#     n, m = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#
#     max_v = 0
#     # 십자
#     for i in range(n):
#         for j in range(n):
#             s = arr[i][j]
#             for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
#                 for k in range(1, m):
#                     ni = i + di * k
#                     nj = j + dj * k
#
#                     if 0 <= ni < n and 0 <= nj < n:
#                         s += arr[ni][nj]
#             if max_v < s:
#                 max_v = s
#     # 대각
#     for i in range(n):
#         for j in range(n):
#             s = arr[i][j]
#             for di, dj in [[1,1], [1,-1], [-1,-1], [-1, 1]]:
#                 for k in range(1, m):
#                     ni = i + di * k
#                     nj = j + dj * k
#
#                     if 0 <= ni < n and 0 <= nj < n:
#                         s += arr[ni][nj]
#             if max_v < s:
#                 max_v = s
#
#     print(f"#{tc} {max_v}")

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    dir1 = [[0,1], [1,0], [0,-1], [-1,0]]
    dir2 = [[1,1], [1,-1], [-1, -1], [-1, 1]]
    max_v = 0

    for i in range(n):
        for j in range(n):
            # 십자
            s = arr[i][j]
            for di, dj in dir1:
                for c in range(1, m):
                    ni = i + di * c
                    nj = j + dj * c
                    if 0 <= ni < n and 0 <= nj < n:
                        s += arr[ni][nj]

            if max_v < s:
                max_v = s

            # 대각
            s = arr[i][j]
            for di, dj in dir2:
                for c in range(1, m):
                    xi = i + di * c
                    xj = j + dj * c

                    if 0 <= xi < n and 0 <= xj < n:
                        s += arr[xi][xj]

            if max_v < s:
                max_v = s

    print(f'#{tc} {max_v}')
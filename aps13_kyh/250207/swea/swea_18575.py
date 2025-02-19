# T = int(input())
# for tc in range(1, T+1):
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#
#     max_v = 0
#     min_v = 100000
#     for i in range(n):
#         for j in range(n):
#             s = arr[i][j]
#             for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
#                 for c in range(1, n):
#                     ni = i + di * c
#                     nj = j + dj * c
#
#                     if 0 <= ni < n and 0 <= nj < n:
#                         s += arr[ni][nj]
#             if max_v < s:
#                 max_v = s
#             if min_v > s:
#                 min_v = s
#
#     print(f"#{tc} {max_v - min_v}")


# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
#
# def get_score(y, x):
#     score = arr[y][x]   # score 초기화 현재 위치
#
#     for i in range(4):  # 방향이 상 하 좌 우
#         ny, nx = y, x   # 현재 위치
#         while True: # 배열 끝까지 터트리기
#             ny += dy[i]
#             nx += dx[i]
#             if 0 <= ny < n and 0 <= nx < n:
#                 score += arr[ny][nx]
#             else:
#                 break
#     return score
#
# T = int(input())
# for tc in range(1, T+1):
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(n)]   # 2차원 배열 : 1차원배열을 n번 반복
#     score1 = float('-inf')   # 최대값
#     score2 = float('inf')   # 최솟값
#     # 행순회 1 : 최대값
#     for y1 in range(n):
#         for x1 in range(n):
#             temp1 = get_score(y1, x1)
#             score1 = max(score1, temp1)
#
#     # 행순회 2 : 최소값
#     for y2 in range(n):
#         for x2 in range(n):
#             temp2 = get_score(y2, x2)
#             score2 = min(score2, temp2)
#
#     result = score1 - score2
#     print(f'#{tc} {result}')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    direction = [[0,1], [1,0], [0,-1], [-1,0]]
    max_v = 0
    min_v = 100000

    for i in range(n):
        for j in range(n):
            s = arr[i][j]
            for di, dj in direction:
                for c in range(1, n):
                    ni = i + di * c
                    nj = j + dj * c

                    if 0 <= ni < n and 0 <= nj < n:
                        s += arr[ni][nj]

            if max_v < s:
                max_v = s
            if min_v > s:
                min_v = s

    print(f'#{tc} {max_v - min_v}')
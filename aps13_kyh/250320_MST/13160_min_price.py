# from collections import deque
#
# def f(N):   # 2차원 다익스트라를 변형된 bfs로 접근
#     D = [[INF] * N for _ in range(N)]
#     D[0][0] = 0
#     q = deque()
#     q.append((0, 0))
#
#     while q:
#         i, j = q.popleft()
#         # i, j 주변에 D가 갱신이 되는지 확인
#         for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
#             ni, nj = i + di, j + dj
#             if 0<= ni < N and 0 <= nj < N:
#                 diff = 0
#                 if arr[ni][nj] > arr[i][j]: # 높은 곳으로 이동하는 경우
#                     diff = arr[ni][nj] - arr[i][j]
#
#                 if D[ni][nj] > D[i][j] + 1 + diff:  # i, j에서 진입하면 절약되는 경우
#                     D[ni][nj] = D[i][j] + 1 + diff
#                     q.append((ni, nj))
#
#     return D[N-1][N-1]
#
#
# INF = int(21e8)
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     print(f"#{tc} {f(N)}")


def dij(N):
    U = [[0] * N for _ in range(N)]     # U = {s}
    D = [[INF] * N for _ in range(N)]   # D = adj[s]

    D[0][0] = 0
    cnt = 0
    while  cnt < N * N:     # 0, 0 인접칸 처리를 편하게 하귀위해 N * N번 반복
        mi = mj = 0         # D[mi][mj]가 최소값 위치 인덱스
        min_v = INF
        for i in range(N):      # U에 포함되지 않고, D가 최소인 칸
            for j in range(N):
                if U[i][j] == 0 and min_v > D[i][j]:
                    mi, mj = i, j
                    min_v = D[i][j]
        U[mi][mj] = 1
        cnt += 1
        for di, dj in [[0,1], [1,0], [-1,0], [0,-1]]:
            ni, nj = mi+di, mj + dj
            if 0 <= ni < N and 0 <= nj < N:
                diff = 0
                if arr[ni][nj] > arr[mi][mj]:
                    diff = arr[ni][nj] - arr[mi][mj]
                D[ni][nj] = min(D[ni][nj], D[mi][mj] + 1 + diff)

    return D[N-1][N-1]


INF = int(21e8)
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(f"#{tc} {dij(N)}")
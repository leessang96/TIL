# def bfs(i, j, n):       # 시작위치 i,j  크기 n
#     visited = [[0] * n for _ in range(n)]   # visited 생성
#     q = []                                  # q 생성
#     q.append((i,j))                         # 시작점 인큐
#     visited[i][j] = 1                       # 시작점 인큐 표시
#                                             # 큐에 남은 칸이 없을때까지... 큐가 비워질때 까지
#     while q:
#         ti, tj = q.pop(0)                   # t <- 디큐
#         if maze[ti][tj] == '3':             # t에서 할 일...
#             # return 1                      # # 출구(3) 에 도착하면 1 아니면 0
#             return visited[ti][tj] - 2      # 입구에서 출구 사이의 빈칸 수
#         # t에 인접 w중, 인큐되지 않은 곳이면
#         direction = [[0,1], [1,0], [0,-1], [-1,0]]
#         for di, dj in direction:
#             wi, wj = ti + di, tj + dj
#             # 미로를 벗어나지 않고, 벽이 아니고
#             if 0 <= wi < n and 0 <= wj < n and maze[wi][wj] != '1' and visited[wi][wj] == 0:
#                 q.append([wi, wj])
#                 visited[wi][wj] = visited[ti][tj] + 1
#         # 인큐, 표시
#     return 0
#
#
# def find_start(n):
#     for i in range(n):
#         for j in range(n):
#             if maze[i][j] == '2':
#                 return i, j
#
# T = int(input())
# for tc in range(1, T+1):
#     n = int(input())        # 미로의 크기
#     maze = [input() for _ in range(n)]
#
#     sti, stj = find_start(n)
#     ans = bfs(sti, stj, n)
#     print(ans)
def bfs(i, j , n):
    visited = [[0] * n for _ in range(n)]       # n * n 배열의 0으로 초기화 해놓고 시작부터 도착까지 거리
    q = []
    q.append((i, j))
    visited[i][j] = 1

    while q:                # 큐가 남아있을때까지
        ti, tj = q.pop(0)            # 디큐해서 인덱스 확인
        if arr[ti][tj] == '3':       # arr의 위치가 3(=도착) 이면 시작점에서 거리 반환
            return visited[ti][tj] - 2
        else:                        # 아니면 방향 돌려가면서 0(=통로) 가 있는 곳으로 이동
            direction = [[0,1], [1,0], [0,-1], [-1,0]]
            for di, dj in direction:
                ni, nj = ti + di, tj + dj

                # n*n 범위를 벗어나지 않고 통로가 1(=벽)이 아닐때와 방문한 적이 없을 때(0) = 즉 이동할 공간이 있다면
                if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] != '1' and visited[ni][nj] == 0:
                    q.append((ni, nj))                          # 해당 인덱스 인큐
                    visited[ni][nj] = visited[ti][tj] + 1       # 시작 위치에서 거리 1 증가

    return 0


def find_start(n):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '2':
                return i, j


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [input() for _ in range(n)]

    sti, stj = find_start(n)
    answer = bfs(sti, stj, n)
    print(f'#{tc} {answer}')

    # visited = [[0] * n for _ in range(n)]
    # q = []
    # q.append((sti, stj))
    # visited[sti][stj] = 1
    # while q:
    #     ti, tj = q.pop(0)       #
    #     if arr[ti][tj] == '3':
    #         cnt = visited[ti][tj] - 2
    #         break
    #     else:
    #         direction = [[0,1], [1,0], [0,-1], [-1,0]]
    #         for di, dj in direction:
    #             wi, wj = ti + di, tj + dj
    #
    #             if 0 <= wi < n and 0 <= wj < n and arr[wi][wj] != '1' and visited[wi][wj] == 0:
    #                 q.append((wi, wj))
    #                 visited[wi][wj] = visited[ti][tj] + 1
    #
    # print(cnt)
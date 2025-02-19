'''
방법 1.
이동가능한 경우 현재 위치 push
'''
# def dfs(i, j, n):
#     stack = []      # 스택 생성
#     visited = [[0] * n for _ in range(n)]   # visited 생성
#     while True:
#         visited[i][j] = 1       # i, j 방문
#         if maze[i][j] == '3':   # 출구
#             return 1            # 성공
#         # i, j 인접한 칸이 벽이 아니고 방문한 적이 없으면 이동
#         for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
#             ni, nj = i+di, j+dj
#             if 0 <= ni < n and 0 <= nj < n and maze[ni][nj] != '1' and visited[ni][nj] == 0:
#                 stack.append((i, j))    # 현재위치 push
#                 i, j = ni, nj           # 이동
#                 break
#         else:   # 갈 수 있는 칸이 없는 경우 break없이 종료하면
#             if stack:   # 경로가 남아있으면
#                 i, j = stack.pop()  # 가장 최근 위치를 꺼내서 이동
#             else:       # 남은 경로가 없으면
#                 # return 0
#                 break   #  while True : 출구에 도착할 수 없는 경우
#     return 0

'''
방법2
스택에 선택가능한 위치를 push
'''
def dfs(i, j, n):
    stack = [(i,j)]          # 갈 수 있는 칸 저장
    visited = [[0] * n for _ in range(n)]        # push 된 칸
    # stack.append((i, j))  # 시작점 push
    visited[i][j] = 1       # 시작점 방문표시
    while stack:            # 갈 수 있는 칸이 남아있으면
        i, j = stack.pop()  # 갈 수 있는 칸을 꺼내서 이동
        if maze[i][j] == '3':
            return 1
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            ni, nj = i + di, j + dj

            if 0 <= ni < n and 0 <= nj < n and maze[ni][nj] != '1' and visited[ni][nj] == 0:
                stack.append((ni, nj))
                visited[ni][nj] = 1   # 스택에 push된 칸, 방문 예정 표시
    return 0        # 출구를 찾지 못하고 끝난경우

def find_start(n):
    for i in range(n):
        for j in range(n):
            if maze[i][j] == '2':
                return i, j
    print('입력오류')
    return -1 -1


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    maze = [input() for _ in range(n)]

    sti, stj = find_start(n)
    ans = dfs(sti, stj, n)
    print(f'#{tc} {ans}')
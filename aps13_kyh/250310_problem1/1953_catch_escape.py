'''
리스트에서 제일 앞에 데이터를 꺼내면 리스트의 길이만큼 시간이 발생
q = [1,2,3]
q.pop(0)    # 0 (리스트의 길이)

1. BFS로 접근
- 이동 방향 : 상하좌우
- 이동이 불가능한 케이스
    - [델타 배열 기본] 범위 밖으로 나가면 못감
    - [방문 기록 기본] 이미 방문한 곳은 안감
    - [문제 조건]
        - 현재 내 위치에서 뚫려있는 곳으로만 이동
        - 다음 가려는 곳의 터널이 뚫려있는 곳으로만 이동
        - 이런 케이스는 델타 배열 순서와 동일하게, 이동 가능 여부를 기록해두면 좋다
2. 방문 기록을 해야한다.(visited)
'''
def bfs(N, M, R, C, L):
    q = [(R, C)]    # 처음 맨홀 뚜껑 위치를 q에 넣기
    visited = [[0] * M for _ in range(N)]
    visited[R][C] = 1 # 시간 처음 맨홀 위치를 1로 기준
    cnt = 0
    while q:        # q가 존재할때까지
        i, j = q.pop(0)
        cnt += 1
        if visited[i][j] < L:   # 방문 시간이 L보다 작으면
            for x in pipe[arr[i][j]]:   # 파이프 모양 확인?
                ni = i + di[x]
                nj = j + dj[x]

                # 0은 터널이 아니므로 지도 범위를 벗어나지 않으며 0이 아니고 / 방문한적이 없으며 /
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 0 and visited[ni][nj] == 0 and (x+2) % 4 in pipe[arr[ni][nj]]:
                    visited[ni][nj] = visited[i][j] + 1
                    q.append((ni, nj))
    return cnt


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
pipe = [[], [0,1,2,3], [1,3], [0,2], [0,3], [0,1], [1,2], [2,3]]

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())   # N 세로, M 가로, R 맨홀 세로 위치, C 맨홀 가로 위치, L = 소요 시간
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = bfs(N, M, R, C, L)
    print("#{} {}".format(tc, answer))

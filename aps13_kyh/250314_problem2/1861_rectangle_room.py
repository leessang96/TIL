# # 정사각형 방 - 정답
# # 접근법
# # N * N visited 배열을 만든다.
# # 해당 숫자에서 갈 수 있다면 1을 기록한다
# # 연속된 1의 길이가 가장 긴 곳이 정답이다.
# # 같은 길이가 있다면, 작은 수가 정답 위치
# dy = [-1,1,0,0]
# dx = [0,0,-1,1]
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     visited = [0] * (N * N + 1)
#
#     # 현재 위치 숫자 기준 상하좌우 확인 -> 1 큰 곳이 있다면 visited 기록
#     for y in range(N):
#         for x in range(N):
#             for i in range(4):  # 상하좌우 확인
#                 ny = y + dy[i]
#                 nx = x + dx[i]
#
#                 # 델타는 범위 밖을 잘 체크해주어야 한다!!!!
#                 if ny < 0 or ny >= N or nx < 0 or nx >= N:
#                     continue
#
#                 if arr[ny][nx] == arr[y][x] + 1:
#                     # 현재 숫자는 다음으로 이동이 가능하다
#                     visited[arr[y][x]] = 1
#                     break # 나머지 방향은 볼 필요 없다.
#
#     # 연속된 1의 개수가 가장 긴 곳을 찾는다.
#     # 가장 긴 곳, 현재 몇 개인지, 출발지
#     max_cnt = cnt = start = 0
#     for i in range(1, N * N + 1):
#         if visited[i] == 1:
#             cnt += 1
#         else:
#             if max_cnt < cnt:
#                 max_cnt = cnt
#                 start = i - cnt
#             cnt = 0
#
#     print(f"#{tc} {start} {max_cnt + 1}")
#
#

direction = [[0,1], [1,0], [0,-1], [-1,0]]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnts = [0] * (N * N + 1)
    for i in range(N):
        for j in range(N):
            for di, dj in direction:
                ni = i + di
                nj = j + dj

                if 0 <= ni < N and 0 <= nj < N and arr[i][j] + 1 == arr[ni][nj]:
                    cnts[arr[i][j]] += 1
                    break

    max_cnt = start = 0
    cnt = 1
    for i in range(N * N + 1):
        if cnts[i] == 1:
            cnt += 1
        else:
            if max_cnt < cnt:
                max_cnt = cnt
                start = i - cnt + 1
            cnt = 1

    print(f"#{tc} {start} {max_cnt}")

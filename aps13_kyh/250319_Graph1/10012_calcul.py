from collections import deque
def bfs(start, end):

    q = deque([start])
    while q:
        t = q.popleft()
        if t == end:
            return visited[t]

        for i in [+1, -1, 2, -10]:
            if i == 2:
                next_t = t * i
            else:
                next_t = t + i

            if 0 < next_t <= 1000000 and not visited[next_t]:
                visited[next_t] = visited[t] + 1
                q.append(next_t)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0] * 1000001
    answer = bfs(N, M)
    print(f"#{tc} {answer}")


# def bfs(N, M):
#     # 큐 생성
#     q = [0] * 1000000
#     visited = [0] * 1000001
#     front = rear = -1
#     rear += 1   # 시작점 인큐
#     q[rear] = N
#     visited[N] = 1  # 시작점 visited 표시
#     while front != rear:    # while q : 큐에 남은 원소가 있으면 반복
#         front += 1
#         t = q[front]
#         if t == M:      # 목표 숫자인 경우
#             return visited[M] - 1
#
#         if t-1 > 0 and visited[t-1] == 0:
#             rear += 1
#             q[rear] = t-1
#             visited[t-1] = visited[t] + 1
#
#         if t+1 <= 1000000 and visited[t+1] == 0:
#             rear += 1
#             q[rear] = t+1
#             visited[t+1] = visited[t] + 1
#         if t*2 <= 1000000 and visited[t*2] == 0:
#             rear += 1
#             q[rear] = t*2
#             visited[t*2] = visited[t] + 1
#         if t-10 > 0 and visited[t-10] == 0:
#             rear += 1
#             q[rear] = t-10
#             visited[t-10] = visited[t] + 1
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#
#     ans = bfs(N, M)
#     print(f"#{tc} {ans}")

# 전형적인 다익스트라 문제
# 1. 최단 거리를 저장할 dists 리스트를 이차원 리스트로 만들어야 한다
#   -> 특정 좌표(y, x)에 갈 때 최단 거리를 저장해야 한다.

# BFS or heapq 정리가 안되면 다익스트라를 받아드리기 어렵다.

import heapq

def dijkstra():
    distance = [[int(21e8)] * N for _ in range(N)]  # 아직 방문하지 않은 노드들 최대값으로 설정
    distance[0][0] = 0  # 시작점 초기화
    pq = [(0,0,0)]  # 누적거리, i, j 좌표

    while pq:
        dist, i, j = heapq.heappop(pq)

        if distance[i][j] < dist:   # 더 짧은 거리가 계산된 노드를 다시 가지 않음
            continue

        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:   # 상하좌우
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:     # 리스트 넘지 않으면
                n_dist = dist + graph[ni][nj]   # 새로운 누적 거리 = 기존거리 + 탐색한거리
                if n_dist < distance[ni][nj]:   # 새로운거리가 기존거리보다 작으면
                    distance[ni][nj] = n_dist   # 기존거리에 누적거리 값 넣고 q에 넣기
                    heapq.heappush(pq, (n_dist, ni, nj))

    return distance[N-1][N-1]   # 끝까지 간 값 반환


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input())) for _ in range(N)]

    result = dijkstra()
    print(f"#{tc} {result}")
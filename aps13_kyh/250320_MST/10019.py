import heapq
INF = int(21e8)
def dijkstra(start):
    pq = [(0, start)]
    distance = [INF] * (N+1)
    distance[start] = 0

    while pq:
        dist, node = heapq.heappop(pq)

        if distance[node] < dist:
            continue

        for next_info in graph[node]:
            next_dist = next_info[0]
            next_node = next_info[1]

            new_dist = dist + next_dist

            if distance[next_node] <= new_dist:
                continue

            distance[next_node] = new_dist
            heapq.heappush(pq, (new_dist, next_node))

    return distance


T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    for _ in range(E):
        start, end, weight = map(int, input().split())
        graph[start].append((weight, end))

    result = dijkstra(0)
    print(f"#{tc} {result[-1]}")
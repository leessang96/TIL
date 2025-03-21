import heapq
def prim(E):
    pq = [(0, 0)]
    visited = [0] * N
    min_c = 0

    cost_list = [float('inf')] * N
    cost_list[0] = 0

    while pq:
        cost, node = heapq.heappop(pq)

        if visited[node]:
            continue

        visited[node] = 1
        min_c += cost

        for next_node in range(N):
            if visited[next_node]:
                continue

            new_cost = ((x_list[next_node] - x_list[node]) ** 2 +
                        (y_list[next_node] - y_list[node]) ** 2) * E

            if new_cost < cost_list[next_node]:
                cost_list[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))

    return round(min_c)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    E = float(input())

    answer = prim(E)
    print(f"#{tc} {answer}")


# kruskal 버전

# def find_set(x):
#     if x == parents[x]:
#         return x
#
#     # 기본코드 : 경로 압축 안한 버전
#     # return find_set(parents[x])
#
#     # 경로 압축 코드
#     parents[x] = find_set(parents[x])
#     return parents[x]
#
#
# def union(x, y):
#     rex = find_set(x)
#     rey = find_set(y)
#
#     if rex == rey:
#         return
#
#     # 디버깅용
#     if rex < rey:
#         parents[rey] = rex
#     else:
#         parents[rex] = rey
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     x_list = list(map(int, input().split()))
#     y_list = list(map(int, input().split()))
#     tax = float(input())
#
#     parents = [i for i in range(N)]
#     min_c = 0
#
#     # 1. 간선들 정보를 모두 저장
#     edges = []
#     for i in range(N):
#         for j in range(i + 1, N):
#             cost = ((x_list[i] - x_list[j]) ** 2 +
#                     (y_list[i] - y_list[j]) ** 2) * tax
#
#     edges.sort(key=lambda x: x[2])
#
#     cnt = 0
#     for u, v, w in edges:
#         if find_set(u) != find_set(v):
#             union(u, v)
#             min_c += w
#             cnt += 1
#         if cnt == N-1:
#             break
#
#     print(f"#{tc} {min_c:.0f}")
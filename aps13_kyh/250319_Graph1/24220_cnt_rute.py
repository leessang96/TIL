def dfs(start, goal):
    global cnt

    if start == goal:
        cnt += 1
        return

    for next_node in graph[start]:
        if visited[next_node]:
            continue

        visited[next_node] = 1
        dfs(next_node, goal)
        visited[next_node] = 0


T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    arr = list(map(int, input().split()))
    S, G = map(int, input().split())

    graph =[[] for _ in range(N + 1)]
    for i in range(0, len(arr), 2):
        graph[arr[i]].append(arr[i+1])  # 단방향 그래프 저장

    cnt = 0
    visited = [0] * (N + 1) # 방문 여부 기록
    visited[S] = 1  # 출발점 초기화
    dfs(S, G)

    print(f"#{tc} {cnt}")
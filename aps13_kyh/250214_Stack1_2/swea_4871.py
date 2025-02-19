T = int(input())
for tc in range(1, T+1):

    def dfs(v):
        stack = []

        while True:
            # if visited[v] == 0:
            visited[v] = 1  # v에 방문 표시
            # v에 인접한 정점중 방문안한 정점 w가 있으면
            for w in adj_list[v]:   # 인접한 정점 w를 꺼내서
                if visited[w] == 0: # 방문한 적이 없으면
                    stack.append(v) # push v
                    v = w           # w에 방문
                    break           # 다른 인접 정점 확인 중단
            else:
                if stack:           # 최근에 지나온 정점으로 복귀, 단, 지나온 정점이 있으면
                    v = stack.pop()
                else:               # 남은 정점이 없으면
                    break           # while T

    V, E = map(int, input().split())
    edge = [list(map(int, input().split())) for _ in range(E)]
    s, g = map(int, input().split())

    adj_list = [[] for _ in range(V+1)]     # 1<= 정점번호 <= N
    # for i in range(E):
    #     adj_list[edge[i][0]].append(edge[i][1])
    for n1, n2 in edge:
        adj_list[n1].append(n2)
        # adj_list[n2].append(n1)
    # s 부터 탐색 후 visited[g]에 방문한 적이 있으면 성공
    visited = [0] * (V + 1)
    dfs(s)
    print(f"#{tc} {visited[g]}")

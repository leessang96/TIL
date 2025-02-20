def bfs(s, g):
    visited = [0] * (V + 1)
    q = []
    q.append(s)
    visited[s] = 1

    while q:
        t = q.pop(0)
        for w in arr[t]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[t] + 1
    if visited[g] == 0:
        return 0
    else:
        return visited[g] - 1


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V+1)]

    for i in range(E):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)

    S, G = map(int, input().split())
    answer = bfs(S, G)

    print(f'#{tc} {answer}')
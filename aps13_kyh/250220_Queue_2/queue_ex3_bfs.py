'''
7 8
4 2 1 2 1 3 5 2 4 6 5 6 6 7 3 7
'''
def bfs(s, v):  # 시작 정점 s, 마지막 정점 v
    visited = [0] * (v + 1) # visited 생성        초기화
    q = []                  # 큐 생성
    q.append(s)             # 시작점 인큐
    visited[s] = 1          # 시작점 인큐 표시
    while q:                # 큐가 비워질 때 까지 반복, front != rear
        t = q.pop(0)                # 디큐해서 t에 저장
        print(t)                    # t정점에 대한 처리
        for w in adj_l[t]:          # t에 인접한 정점 w 중, 인큐되지 않은 정점이 있으면
            if visited[w] == 0:
                q.append(w)         # 인큐하고, 인큐 표시
                visited[w] = visited[t] + 1
    print(visited)

V, E = map(int, input().split())        # 1번부터 v번 정점, e개의 간선
arr = list(map(int, input().split()))

# 인접리스트 --------------------
adj_l = [[] for _ in range(V+1)]
# for i in range(0, E*2, 2):
#     v1, v2 = arr[i], arr[i+1]
#     adj_l[v1].append(v2)
#     adj_l[v2].append(v1)
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)    # 방향이 없는 경우

print(adj_l)
bfs(1, 7)
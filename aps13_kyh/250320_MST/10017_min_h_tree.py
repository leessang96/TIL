def find_set(x):
    while parents[x] != x:  # 대표원소를 찾을 때 까지
        x = parents[x]
    return x


def union(x, y):
    parents[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edge = [list(map(int, input().split())) for _ in range(E)]

    # Kruskal 적용
    # 가중치 기준 오름차순 정렬
    edge.sort(key=lambda x: x[2])

    # 서로소 집합 (대표원소 집합)
    parents = [i for i in range(V+1)]   # 0번부터 V번까지의 노드

    # 0 ~ V번 정점, 정점수 V+1개, 신장트리의 간선 수 V개
    cnt = 0 # 선택한 간선 수
    total = 0
    for n1, n2, w in edge: # 오름차순 정렬된 순으로 꺼내서
        # 싸이클 확인
        if find_set(n1) != find_set(n2):
            total += w
            union(n1, n2)
            cnt += 1

        if cnt == V: # MST 구성완료
            break

    print(f"#{tc} {total}")
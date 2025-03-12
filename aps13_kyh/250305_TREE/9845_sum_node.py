def f(n):
    if n > N:           # 존재하지 않는 경우 0 리턴
        return 0
    if tree[n] != 0:    # 리프노드에 값이 들어있으므로 리프노드인 경우
        return tree[n]
    else:
        r1 = f(n*2)     # 왼쪽 자식 노드의 값
        r2 = f(n*2+1)   # 오른쪽 자식노드의 값
        tree[n] = r1 + r2
        return tree[n]


T = int(input())
for tc in range(1, T+1):
    # 노드 개수 N, 리프 노드 개수 M, 값 출력 노드 번호 L
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)

    for _ in range(M):
        node, value = map(int, input().split())
        tree[node] = value

    f(1)
    print(f"#{tc} {tree[L]}")
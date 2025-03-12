for tc in range(1, 11):
    N = int(input())        # 정점 개수 N
    tree = [0] * (N+1)

    for _ in range(N):
        node, oper, *child = map(input().split())

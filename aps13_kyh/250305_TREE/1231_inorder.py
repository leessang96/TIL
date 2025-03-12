# def in_order(n):
#     if n <= N:      # 최대 정점 번호 이내인 경우 유효
#         in_order(n*2)   # 왼쪽 자식
#         print(tree[n], end='')
#         in_order(n*2+1) # 오른쪽 자식으로 이동
#
#
# for tc in range(1, 11):
#     N = int(input())
#     tree = [0] * (N+1)
#     for _ in range(N):
#         v, c, *child = input().split()
#         # arr = input().split()
#         tree[int(v)] = c    # 완전이진트리
#
#     print(f"#{tc}", end=' ')
#     in_order(1) # 루트부터 중위순회
#     print()
def in_order(n):
    if n <= N:
        in_order(n*2)
        print(tree[n], end='')
        in_order(n*2+1)


for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N+1)

    for _ in range(N):
        arr = input().split()
        tree[int(arr[0])] = arr[1]

    print(f"#{tc}", end=' ')
    in_order(1)
    print()










































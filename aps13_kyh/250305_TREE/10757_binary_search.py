# def in_order(n):
#     global num
#     if n <= N:
#         in_order(n*2)
#         tree[n] = num
#         num += 1
#         in_order(n*2+1)
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())        # 1부터 n까지의 자연수에 해당할 N
#     tree = [0] * (N+1)
#     num = 1
#     in_order(1)
#
#     print(f"#{tc} {tree[1]} {tree[N//2]}")
def f(i, a):        # 왼쪽에 위치한 조상의 순서 a
    if i > N:       # 완전이진트리
        return 0    # 서브트리의 정점 0개
    else:
        l = f(i*2, a)   # l 서브트리의 정점 개수 리턴
        tree[i] = l + a + 1
        r = f(i*2+1, tree[i])
        return l+r+1


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    tree = [0] * (N+1)
    cnt = 1
    f(1, 0)
# T = int(input())
# for tc in range(1, T+1):
#     n, q = map(int, input().split())
#     arr = [0] * n
#
#     for i in range(1, q+1):
#         l, r = map(int, input().split())
#
#         for j in range(l-1, r):   # 0, 1, 2
#             arr[j] = i
#
#     print(f"#{tc}", *arr)

T = int(input())
for tc in range(1, T+1):
    n, q = map(int, input().split())
    arr = [0] * n

    for _ in range(q):
        l, r = map(int, input().split())

        for i in range(l-1, r):
            arr[i] = _ + 1
    print(f'#{tc}', *arr)
































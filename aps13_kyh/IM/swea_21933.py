# T = int(input())
# for tc in range(1, T+1):
#     n, m = map(int, input().split())
#
#     a = list(map(int, input().split()))
#     b = list(map(int, input().split()))
#
#     c = [0] * (n + m)
#     i = j = 0
#     while  i + j < n + m:
#         if i < n:
#             c[i+j] = a[i]
#             i += 1
#         if j < m :
#             c[i+j] = b[j]
#             j += 1
#
#     print(f"#{tc}", *c)


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    c = [0] * (len(a) + len(b))

    i = j = 0
    while i + j < n + m:
        if i < n:
            c[i+j] = a[i]
            i += 1
        if j < m:
            c[i+j] = b[j]
            j += 1

    print(f'#{tc}', *c)
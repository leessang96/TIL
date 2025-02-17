# T = int(input())
# for tc in range(1, T+1):
#     n = int(input())
#
#     a = list(map(int, input().split()))
#     b = list(map(int, input().split()))
#
#     cnt = 0
#     for i in range(n):
#         if a[i] != b[i]:
#             cnt += 1
#             for j in range(i, n):
#                 if b[j]:
#                     b[j] = 0
#                 else:
#                     b[j] = 1
#                 # b[j] = 0 if b[j] else 1
#     print(f"#{tc} {cnt}")

'''
3
3
0 0 0
0 1 0
5
0 1 1 0 0
0 0 0 1 1
10
1 1 1 1 1 0 0 0 1 1
1 1 0 1 1 0 1 1 0 0
'''

T = int(input())
for tc in range(1, T+1):
    n = int(input())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    cnt = 0
    for i in range(n):
        if a[i] != b[i]:
            cnt += 1
            for j in range(i, n):
                if a[j] == 0:
                    a[j] = 1
                else:
                    a[j] = 0

    print(f'#{tc} {cnt}')
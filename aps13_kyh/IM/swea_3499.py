# def get_result():
#     a = 0
#     b = (len(arr) + 1) // 2
#
#     for turn in range(len(arr)):
#         if turn % 2 == 0:
#             print(arr[a], end=' ')
#             a += 1
#         else:
#             print(arr[b], end=' ')
#             b += 1
#
# T = int(input())
# for tc in range(1, T+1):
#     n = int(input())
#     arr = list(input().split())
#     print(f'#{tc}', end = ' ')  # 줄 바꿈 안되게
#     get_result()
#     print()


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(input().split())

    a = 0
    b = (len(arr) + 1) // 2

    print(f'#{tc}', end=' ')
    for i in range(len(arr)):
        if i % 2 == 0:
            print(arr[a], end=' ')
            a += 1
        else:
            print(arr[b], end=' ')
            b += 1

    print()
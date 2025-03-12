# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     price_lst = list(map(int, input().split())) + [0]
#
#     buy = 0
#     sell = 0
#     day = 0
#     for i in range(1, len(price_lst)):
#         if price_lst[i-1] > price_lst[i]:
#             sell += price_lst[i-1] * day - buy
#             day = 0
#             buy = 0
#         elif price_lst[i] >= price_lst[i-1]:
#             buy += price_lst[i-1]
#             day += 1
#
#     print(f"#{tc} {sell}")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    price_list = list(map(int, input().split()))

    buy = 0
    max_b = 0
    for i in reversed(price_list):
        if buy < i:
            buy = i
        else:
            max_b += buy - i

    print(f"#{tc} {max_b}")
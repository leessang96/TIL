# test case 1개인 경우
'''
1
2
1 3
2 5
5
1
2
3
4
5
'''
# test case 2개인 경우
'''
2
2
1 3
2 5
5
1
2
3
4
5
2
1 3
2 5
5
1
2
3
4
5000
'''

# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     # arr = list(map(int, input())))
#     count = [0] * 5001
#
# # [_ 참고자료](https://mingrammer.com/underscore-in-python/)
#     for _ in range(N):
#         Ai, Bi = map(int, input().split())  # Ai부터 Bi까지 운행
#         for i in range(Ai, Bi + 1):
#             count[i] += 1                   # count[i] 정류장을 지나는 경우
#
#     print(f'#{tc}', end = ' ')
#     P = int(input())
#     for _ in range(P):
#         n = int(input())
#         print(count[n], end = ' ')
#     print()           # 지금은 test case 하나라 상관없지만, 여러개면 이거 써야함



T = int(input())
for tc in range(1, T+1):
    n = int(input())
    stops = [0] * 5001

    for _ in range(n):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            stops[i] += 1

    print(f"#{tc}", end = ' ')
    p = int(input())
    for _ in range(p):
        c = int(input())
        print(stops[c], end = ' ')


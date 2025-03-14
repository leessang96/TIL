# # level : 점원 수
# # branch : 탑에 포함 시킨다 or 안시킨다
#
# def recur(cnt, total_height):
#     global answer
#     # 기저조건 가지치기
#     # 이미 B 이상인 탑이면, 점원을 더 쌓을 필요가 없다.
#     # => 탑이 더 높은 정답은 필요 없다.
#     if total_height >= B:
#         answer = min(answer, total_height)
#         return
#
#     if cnt == N:
#         return
#
#     recur(cnt + 1, total_height + heights[cnt]) # 탑에 포함 시키는 경우
#     recur(cnt + 1, total_height) # 탑에 포함 안시키는 경우
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N, B = map(int, input().split())        # N 점원 수, B 탑 높이
#     heights = list(map(int, input().split()))   # 점원 리스트
#     answer = int(21e8)   # 21억
#     recur(0, 0)
#     print(f"#{tc} {answer-B}")









def recur(cnt, total_height):   # 사람 수 올리는 cnt, 사람 수에 맞게 키 더해주기
    global min_h

    if total_height >= B:
        min_h = min(min_h, total_height)
        return

    if cnt == N:
        return

    recur(cnt + 1, total_height + height[cnt])
    recur(cnt + 1, total_height)


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    min_h = int(21e8)
    recur(0, 0)
    print(f"#{tc} {min_h - B}")
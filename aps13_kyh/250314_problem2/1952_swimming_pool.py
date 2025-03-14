# # 완전 탐색을 하는 버전
# # 각 달에 4가지 케이스를 모두 확인하면서 진행
# def recur(month, total_cost):
#     global min_answer
#
#     if min_answer < total_cost:
#         return
#
#     if month > 12:
#         min_answer = min(min_answer, total_cost)
#         return
#
#     # 1일권으로 다 사는 경우
#     recur(month + 1, total_cost + (days[month] * cost_day))
#     # 1달권으로 사는 경우
#     recur(month + 1, total_cost + cost_month)
#     # 3달권으로 사는 경우
#     recur(month + 3, total_cost + cost_month3)
#     # 1년 이용권 사는 경우
#     recur(month + 12, total_cost + cost_year)
#
#
# T = int(input())
# for tc in range(1, T+1):
#     # 이용권 가격들 (1일, 1달, 3달, 1년)
#     cost_day, cost_month, cost_month3, cost_year = map(int, input().split())
#     # 12개월 이용 계획
#     days = [0] + list(map(int, input().split()))
#     min_answer = int(21e8)
#     recur(1, 0)
#     print(f"#{tc} {min_answer}")

'''
DP 문제 접근법
1. TOP-DOWN 방식
    - DP(메모이제이션)
    - 거듭제곱 문제

2. Bottom-UP 방식
    - 시작점을 정해둔다
    - 앞으로 쌓아 가면서 진행
    - 기존값을 활용
    - 정답을 계산해서 저장하면서 진행
    -> 점화식을 구하는 경우가 많다.

'''


# T = int(input())
# for tc in range(1, T+1):
#     cost_day, cost_month, cost_month3, cost_year = map(int, input().split())
#     days = [0] + list(map(int, input().split()))
#
#     dp = [0] * 13
#     # 시작점 초기화 (1월, 2월)
#     # 1월의 가격 (1일권 구매 vs 1달권 구매)
#     dp[1] = min(days[1] * cost_day, cost_month)
#     # 2월의 가격 = 1월의 가격 + (1일권 구매 vs 1달권 구매)
#     dp[2] = dp[1] + min(days[2] * cost_day, cost_month)
#
#     # 3월 ~ 12월은 반복하면서 계산
#     for month in range(3, 13):
#         # N월의 최소 비용 후보
#         # 1. N-3월에 3개월 이용권을 구입한 경우
#         # 2. N-1월의 최소 비용 + 1일권 구매
#         # 3. N-1월의 최소 비용 + 1달권 구매
#         dp[month] = min(dp[month-3] + cost_month3
#                         , dp[month-1] + (days[month] * cost_day)
#                         , dp[month-1] + cost_month)
#
#     # 12월의 누적 최소 금액 vs 1년권
#     answer = min(dp[12], cost_year)
#     print(f"#{tc} {answer}")


def f(i, s):    # i월에 수영장을 다니는 방벙을 결정, s 이전까지의 비용
    global min_v # cnt
    #cnt += 1
    if i > 12:  # 12월까지 다니는 비용이 다 결제된 경우
        if min_v > s:
            min_v = s
    elif min_v <= s:
        return
    else:
        f(i+1, s + min(day * use[i], month))
        f(i+3, s + month3)


T = int(input())
for tc in range(1, T+1):
    day, month, month3, year = map(int, input().split())
    use = [0] + list(map(int, input().split())) # 월별 이용일, 1월~12월

    min_v = year        # 1년권 비용으로 초기화
    #cnt = 0
    f(1, 0)
    print(f"#{tc} {min_v}")
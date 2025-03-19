# level : N개의 원소를 모두 고려하면
# branch : 집합에 해당 원소를 포함 시키는 경우 or 안시키는 경우
# 누적값
#   - 부분집합의 총합
#   - 부분집합에 포함된 원소들
def dfs(cnt, total, subset):
    # 1. total이 10이면 반환
    if total == 10:
        print(subset)
        return

    # 2. total 이 10을 넘기면 가지치기 하자
    if total > 10:
        return

    if cnt == 10:
        return

    dfs(cnt + 1, total + arr[cnt], subset + [arr[cnt]])  # 포함 하는 경우
    dfs(cnt + 1, total, subset) # 안하는 경우


arr = [i for i in range(1, 11)]
visited = []
dfs(0,0,[])

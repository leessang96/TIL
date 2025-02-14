T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]

    max_v = 0
    # 가로로 연속한 1의 개수
    for i in range(n):
        cnt = 0             # 행이 바뀌면 1의 개수 초기화
        for j in range(m):
            if arr[i][j] == 1:
                cnt += 1
                if max_v < cnt:
                    max_v = cnt
            else:
                cnt = 0

    for j in range(m):
        cnt = 0
        for i in range(n):
            if arr[i][j] == 1:
                cnt += 1
                if max_v < cnt:
                    max_v = cnt
            else:
                cnt = 0

    if max_v == 1:       # 노이즈만 있는 경우
        max_v = 0

    print(f"#{tc} {max_v}")

T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    puzzle = [list(map(int, input().split())) + [0] for _ in range(n)] + [[0] * (n+1)]

    num = 0
    temp = 0
    for i in range(n):
        for j in range(n+1):
            if puzzle[i][j] == 1:
                temp += 1
            else:
                if temp == k:
                    num += 1
                temp = 0

    for i in range(n):
        for j in range(n+1):
            if puzzle[j][i] == 1:
                temp += 1
            else:
                if temp == k:
                    num += 1
                temp = 0

    print(f'#{tc} {num}')


def is_babygin():
    tri = run = 0
    if p[0] == p[1] == p[2]:
        tri += 1
    if p[3] == p[4] == p[5]:
        tri += 1
    if p[0] + 2 == p[1] + 1 == p[2]:
        run += 1
    if p[3] + 2 == p[4] + 1 == p[5]:
        run += 1

    if tri + run == 2:
        return True


def f(i, N):
    global answer
    if i == N:
        if is_babygin():
            answer = "Baby Gin"
    else:
        for j in range(N):
            if used[j] == 0:
                used[j] = 1
                p[i] = arr[j]
                f(i+1, N)
                used[j] = 0


T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input()))
    used = [0] * 6
    p = [0] * 6
    answer = "Lose"
    f(0,6)
    print(f"#{tc} {answer}")
di = [0, 1, 0, -1]     # 오른쪽부터 시계방향으로
dj = [1, 0, -1, 0]     #

# 2행 3열
i = 2
j = 3

for dir in range(4):
    ni = i + di[dir]
    nj = j + dj[dir]
    print(ni, nj)

# 뭐지? 강의 참고
N = 2
M = 3
for i in range(N):
    for dir in range(4):
        ni = i + di[dir]
        nj = j + dj[dir]
        if 0 <= ni < N and 0 <= nj < M:
            print(ni, nj)












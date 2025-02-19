'''
5
45 15 10 56 23
96 98 99 40 69
96 84 49 46 34
16 64 81 4 11
10 66 85 55 14

'''
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
total = 0
for i in range(N):
    for j in range(N):
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N:
                total += abs(arr[ni][nj] - arr[i][j])
print(total)
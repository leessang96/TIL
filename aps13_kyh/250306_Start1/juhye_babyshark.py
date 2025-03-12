def find_start_idx(n):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 9:
                arr[i][j] = 0
                return i, j


def find_short_distance(si, sj, n):
    visited = [[0]*n for _ in range(n)]
    direction = [[0, -1], [-1, 0], [1, 0], [0, 1]]
    q = []
    q.append([si, sj])
    size = 2
    visited[si][sj] = 1
    count = 0
    result = 0
    while q:
        ti, tj = q.pop(0)
        for di, dj in direction:
            ni, nj = ti + di, tj + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] <= size:
                if 0 < arr[ni][nj] < size:  # 먹기
                    arr[ni][nj] = 0
                    count += 1
                    visited[ni][nj] = visited[ti][tj] + 1
                    result += visited[ni][nj] - 1
                    q = []
                    q.append([ni, nj])
                    visited = [[0] * n for _ in range(n)]
                    visited[ni][nj] = 1
                    if count == size:
                        count = 0
                        size += 1
                else:  # 0 이거나 size 값과 같으면
                    q.append([ni, nj])
                    visited[ni][nj] = visited[ti][tj] + 1
                flag = 1
                for i in range(n):
                    for j in range(n):
                        if 0 < arr[i][j] < size:
                            flag = 0
                            break
                if flag == 1:
                    return result

    return result


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
sti, stj = find_start_idx(N)
print(find_short_distance(sti, stj, N))


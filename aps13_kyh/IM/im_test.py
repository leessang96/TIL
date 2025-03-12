'''
3
5
19 57 74 73 94
26 27 32 98 61
40 88 49 38 25
21 66 53 95 46
80 23 58 39 89
7
40 49 56 83 84 31 11
42 95 12 16 21 19 26
98 93 29 68 10 92 82
23 13 24 58 35 25 47
17 66 39 67 70 14 87
22 34 46 94 69 96 89
62 88 50 51 61 71 86
9
90 57 65 18 25 93 64 11 54
95 19 80 37 63 44 15 14 10
89 59 46 70 38 36 21 51 97
53 47 60 88 40 48 79 56 55
83 13 27 86 45 71 75 28 84
30 20 29 35 99 98 61 94 23
85 42 43 22 16 77 31 78 34
74 26 73 92 50 72 87 49 32
68 24 91 12 17 82 69 67 81#1 6

#2 10

#3 9
'''
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_route = 0
    for i in range(n):
        for j in range(n):
            route = 1
            ci, cj = i, j
            while True:
                min_x, min_y = ci, cj
                for di, dj in [[0,1], [0,-1], [1,0], [-1,0]]:
                    ni, nj = ci + di, cj + dj

                    if 0 <= ni < n and 0 <= nj < n:
                        if arr[i][j] < arr[ni][nj]:
                            continue
                        elif arr[ni][nj] < arr[min_x][min_y]:
                            min_x = ni
                            min_y = nj
                if min_x == ci and min_y == cj:
                    break
                else:
                    route += 1
                    ci, cj = min_x, min_y
                    if max_route < route:
                        max_route = route

    print(f"#{tc} {max_route}")
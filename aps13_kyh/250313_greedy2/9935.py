T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    cnt = 1

    for _ in range(N):
        s, e = map(int, input().split())
        arr.append((s, e))

    arr.sort(key= lambda x: x[1])

    # arr[i][1] 이 가장 낮은 값을 찾아서 저장
    end = arr[0][1]

    for i in range(N):
        if arr[i][0] >= end:
            cnt += 1
            end = arr[i][1]

    print(f"#{tc} {cnt}")


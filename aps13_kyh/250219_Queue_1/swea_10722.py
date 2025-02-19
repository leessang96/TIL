T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    rear = 0
    for i in range(m):
        rear = (rear + 1) % n
    print(f'#{tc} {arr[rear]}')
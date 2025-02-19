# 주어진 N 길이의 숫자열을 오름차순으로 정렬하여 출력하라
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    # 선택 정렬
    for i in range(n-1):
        min_v = i
        for j in range(i+1, n):
            if arr[min_v] > arr[j]:
                min_v = j
        arr[i], arr[min_v] = arr[min_v], arr[i]

    print(f"#{tc}", *arr)

    # 버블 정렬
    # for i in range(n):
    #     for j in range(1, n):
    #         if arr[j-1] > arr[j]:
    #             temp = arr[j-1]
    #             arr[j-1] = arr[j]
    #             arr[j] = temp
    #
    # print(f"#{tc} {arr}")

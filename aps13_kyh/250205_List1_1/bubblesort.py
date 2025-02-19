'''
6
2 7 5 3 1 4
'''

def bubblesort(arr, N):
    for i in range(N - 1, 0, -1):           # 정렬구간의 끝 i
        for j in range(i):                  # 비교하는 왼쪽 원소의 인덱스(0부터 구간 마지막 인덱스 -1 까지)
            if arr[j] > arr[j + 1]:         # 왼쪽 원소가 크면 자리 교환
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

N = int(input())
arr = list(map(int, input().split()))
bubblesort(arr, N)
print(arr)
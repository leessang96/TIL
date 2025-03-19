def merge(left, right):
    # 두 리스트를 병합한 결과 리스트
    result = [0] * (len(left) + len(right))
    l = r = 0

    # 두 리스트에서 비교할 대상이 남아있을 때 까지 반복
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l + r] = left[l]
            l += 1
        else:
            result[l + r] = right[r]
            r += 1

    # 왼쪽 리스트에 남은 데이터들을 모두 result 에 추가
    while l < len(left):
        result[l + r] = left[l]
        l += 1
    # 오른쪽 리스트에 남은 데이터들을 모두 result 에 추가
    while r < len(right):
        result[l + r] = right[r]
        r += 1

    return result


def merge_sort(arr):
    global cnt
    if len(arr) == 1:
        return arr

    # 1. 절반 씩 분할
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left_list = merge_sort(left)
    right_list = merge_sort(right)
    if left_list[-1] > right_list[-1]:
        cnt += 1

    # 분할이 완료되면
    # 2. 병합
    merged_list = merge(left_list, right_list)
    return merged_list


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = list(map(int, input().split()))
    cnt = 0
    sorted_arr = merge_sort(L)
    print(f"#{tc} {sorted_arr[N//2]} {cnt}")


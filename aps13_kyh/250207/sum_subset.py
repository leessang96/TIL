'''
3
3 6
5 15
5 10

'''
T = int(input())
for tc in range(1, T + 1):
    N, K = list(map(int, input().split()))
    # N: # of subset_component
    # K: sum of subset
    # print(N, K)
    # print()
    arr = [x for x in range(1, 13)]     # 집합 A는 1 ~ 12의 숫자를 원소로 가짐
    # print(arr)
    n = len(arr)

    result_set = []
    result_subset = []
    # N 개의 원소를 가진 subset 생성(bitwise operators 이용)
    for i in range(1 << n):
        temp = []       # 부분집합을 생성할 임시 리스트 생성
        for j in range(n):
            if i & (1 << j):
                # print(arr[j], end = ' ')
                temp.append(arr[j])
            # print(temp)
        # print(temp)
        # 임시 리스트 중, 원소의 개수가 조건에 맞는 경우만 부분집합으로 넣기
        if len(temp) == N:
            result_subset.append(temp)
    # print(result_subset)
    
    # 개수는 만족했으니, 합이 조건에 맞는 경우를 구하자
    for x in result_subset:
        sum_subset = 0
        for y in x:
            sum_subset += y
        if sum_subset == K:
            result_set.append(result_subset)
    # print(result_set)
    # print(result_subset)
    # print(len(result_set))
    print(f'#{tc} {len(result_set)}')


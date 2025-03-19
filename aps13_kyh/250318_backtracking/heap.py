import heapq

arr = [20, 15, 19, 4, 13, 11]

# 1. 기본 리스트를 heap으로 만들기
heapq.heapify(arr)  # 최소힙으로 바뀐다.
# 디버깅 시에 이진 트리로 그림을 그려야 함
# -> 딱 봤을때는 정렬이 안된 것 처럼 보임
# print(arr)

# 2. 하나 씩 데이터를 추가
min_h = []
for num in arr:
    heapq.heappush(min_h, num)

print(min_h)

# 최대힙?
max_h = []
for num in arr:
    heapq.heappush(max_h, -num)

while max_h:
    pop_num = heapq.heappop(max_h)
    print(-pop_num, end=' ')

# 1. 길이 순서로 먼저 출력
# 2. 길이가 같다면, 사전 순으로 출력
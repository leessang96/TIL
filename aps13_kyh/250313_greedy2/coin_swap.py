# coin_list = [500, 100, 50, 10]  # 큰 동전부터 앞으로 작성함
# target = 1730
# cnt = 0
#
# for coin in coin_list:
#     possible_cnt = target // coin   # 현재 동전으로 가능한 최대 수
#     cnt += target // coin           # 정답에 더해준다.
#     target -= coin * possible_cnt   # 금액을 빼준다.
#
# print(cnt)

# people = [15, 30, 50, 10]
# n = len(people)
#
# # 접근법. 최소 시간인 사람부터 화장실로 들어가자
# people.sort()   # 오름차순 정렬
# total_time = 0  # 전체 대기 시간
# remain_people = n - 1   # 대기인원 수
#
# for turn in range(n):
#     time = people[turn]
#     total_time += time * remain_people
#     remain_people -= 1
#
# print(total_time)

n = 3
target = 30
things = [(5, 50), (10, 60), (20, 140)] # (kg, price)

# kg 당 가격으로 어떻게 정렬?
# 정렬 : (price / kg)
# lambda: 재사용하지 않는 함수
things.sort(key=lambda x: (x[1] / x[0]), reverse=True)
print(things)


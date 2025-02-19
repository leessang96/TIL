'''
0 <= DATA[i] <= 4 조건
'''

DATA = [0, 4, 1, 3, 1, 2, 4, 1]
N = len(DATA)
COUNTS = [0] * 5        # max(DATA) + 1, 크기에 주의!!
# COUNTS 만들때 주의!!
# n = len(DATA)
# COUNTS = [0] * N
# 이러면 작동되는것 처럼 보이는데.. 아님

# 아까 조건 대충 넘어갔는데
# 카운팅 정렬은 내가 정렬할 대상이 인덱스로 표현할 수 없으면 사용 불가
# 음수는 일정 값을 더하는 방법이 있는데, 굳이?
# 그래서 조건 0 이상
# 알고리즘 문제는 보통 1,000,000(백만)까지 숫자, 0부터
# 나중에 퀵소트, 머지까지 하면 백만개 대상으로 하는거 보여줌

# 일단은... 배열의 범위가 가능해 / 카운팅 정렬로 해! 라는 문제만 ㄱㄱ
# 음수는 나중에 생각
TEMP = [0] * N           # 원본의 개수와 같아야 함. 최종 정렬 결과 저장

for i in range(N):
    COUNTS[DATA[i]] += 1
# print(COUNTS)           # [1, 3, 1, 1, 2]
for i in range(1, 5):       # COUNTS[i] 까지의 합계
    COUNTS[i] += COUNTS[i - 1]

# print(COUNTS)               # [1, 4, 5, 6, 8]
for i in range(N - 1, -1, -1):
    COUNTS[DATA[i]] -= 1        # DATA[i] 까지의 개수 1개 감소
    # DATA[i]까지 차지한 칸 수 중 가장 오른쪽에 DATA[i] 기록
    TEMP[COUNTS[DATA[i]]] = DATA[i]

print(TEMP)







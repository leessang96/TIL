T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())        # 화덕의 크기 n과 피자 개수 m
    c = list(map(int, input().split()))     
    
    # oven = []
    # for i in range(n):  # n개의 피자를 처음으로 넣기
    #     oven.append(i)
    # oven = [i for i in range(n)]    # 오븐 초기화
    # next = n        # 다음 차례로 투입할 피자 인덱스
    # finish = -1     # 방금 완성된 피자 인덱스
    # while oven:
    #     finish = oven.pop(0) # 현재 상태 가장 앞의 피자
    #     c[finish] //= 2      # 치즈 절반 녹음
    #     if c[finish] == 0 :  # 완성
    #         finish = finish  # 방금 완성된 피자 번호 기록
    #         # 남은 피자 투입
    #         if next < m :   # 남은 피자 투입
    #             oven.append(next)
    #             next += 1
    #     else:               # 치즈가 남았으면 다시 투입
    #         oven.append(finish)
    # print(f'#{tc} {finish+1}')

    # oven = [0] * (n+1)
    # front = 0
    # rear = 0
    # dough = n
    # door = 0
    # for i in range(n):
    #     rear = (rear+1) % (n+1)
    #     oven[rear] = i
    # 
    # while front != rear:
    #     front = (front + 1) % (n+1)
    #     door = oven[front]
    #     c[door] //= 2
    #     if c[door] > 0:
    #         rear = (rear+1) % (n+1)
    #         oven[rear] = door
    #     else:
    #         if dough < m:
    #             rear = (rear+1) % (n+1)
    #             oven[rear] = dough
    #             dough += 1
    # 
    # print(f'#{tc} {door+1}')
        
    oven = [i for i in range(n)]    # 초기 투입상태
    door = 0    # 화덕의 도어에 도착한 오븐의 인덱스
    cnt = 0     # 화덕에서 꺼내진 개수
    last = 0    # 최근에 꺼낸 피자 인덱스
    next = n
    while cnt < m:      # 모든 피자가 완성되지 않은 경우
        if oven[door] != -1:
            last = oven[door]  # 입구에 도달한 피자를 꺼내서
            c[last] //= 2  # 꺼내진 피자는 치즈가 절반으로 줄고
            if c[last] == 0:     # 완성된 경우
                cnt += 1         # 추가
                if next < m:     # 남은 피자가 있으면
                    oven[door] = next
                    next += 1
                else:
                    oven[door] = -1 # 남은 피자가 없으면 빈자리
        door = (door + 1) % n
    print(f'#{tc} {last+1}')


    
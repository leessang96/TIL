# T = 10
# for _ in range(T):
#     tc = int(input())
#     ladder = [[0] * 102] + [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
# 
#     start = 0
#     for j in range(101):    # 도착점 찾기
#         if ladder[99][j] == 2:
#             start = j
#             break
#     
#     # 왼쪽, 오른쪽 우선 둘 다 0이면 위로
#     i, j =  99, start
#     while i >= 0:   # 맨 위가 아니면 
#         while ladder[i][j-1]:       # 왼쪽으로 이동가능하면
#             ladder[i][j] = 0        # 지나간 위치 지우기
#             j -= 1                  # 왼쪽으로 이동
#         while ladder[i][j+1]:       # 오른쪽으로 이동가능하면
#             ladder[i][j] = 0        # 지나간 위치 지우기
#             j += 1                  # 오른쪽으로 이동
#         i -= 1
# 
#     print(f"#{tc} {j-1}")
# 

'''
1 0 0 0 1 0 1 0 0 1
1 0 0 0 1 0 1 1 1 1
1 0 0 0 1 0 1 0 0 1
1 0 0 0 1 1 1 0 0 1
1 0 0 0 1 0 1 0 0 1
1 1 1 1 1 0 1 1 1 1
1 0 0 0 1 0 1 0 0 1
1 1 1 1 1 0 1 0 0 1
1 0 0 0 1 1 1 0 0 1
1 0 0 0 1 0 1 0 0 2

'''
def move():     # 100 * 100 사다리 타기
    for start in range(100):
        if ladder[0][start]:    # 세로막대가 있는 위치에서 출발
            i = 0
            j = start
            v = [[0] * 100 for _ in range(100)]     # 지나간 위치를 표시
            while i < 100:
                while j-1 >= 0 and ladder[i][j-1] and v[i][j-1] == 0: # 왼쪽
                    v[i][j] = 1     #지나간 위치를 표시
                    j -= 1
                while j+1 <= 99 and ladder[i][j+1] and v[i][j+1] == 0: # 오른쪽
                    v[i][j] = 1
                    j += 1
                
                i += 1  # 아래로
            if ladder[99][j] == 2:
                return start
    return -1   # 디버깅 목적
                                                                    

T = 10
for _ in range(T):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    
    answer = move()
    print(f"#{tc} {answer}")
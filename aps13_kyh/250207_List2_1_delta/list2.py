'''
3
1 2 3
4 5 6
7 8 9

'''
N = int(input())        # 배열 행과 열의 크기  N:3
arr = [list(map(int, input().split())) for _ in range(N)]

print(arr)

arr2 = [[0] * N for _ in range(N)]
print(arr2)

# 이렇게 하면 안됨!
arr3 = [[0] * 4] * 3
print(arr3)
# 2행 1열만 바꾸고 싶은데..
arr3[2][1] = 1
print(arr3)     # 모든행이 바뀌네??
# 이건, [[0]] * 4]로 만든 객체에 참조를 3번 해! 라는 것과 같은 얘기
# 일종의 얕은복사

for i in range(N):
    for j in range(N):
        print(arr[i][j])

# num = 456789
num = int(input())
c = [0] * 12     # c[10], c[11]은 항상 0, run 확인을 위한 여분

for _ in range(6):      # 단순 반복 6회
    c[num % 10] += 1        # num % 10: 1의 자리 알아내기
    num //= 10              # num의 1의 자리 제거 축약형
# print(c)
# 파이참을 쓰는 이유: 디버거 써보라고
# 8줄(print(c)에 종단점 두고 디버깅 런 누르면 콘솔에 >? 뜸
# 여기 값 넣으면 됨

i = 0
tri = run = 0
while i < 10:       # 카드 번호가 9까지.. <= 9 해도됨
    if c[i] >= 3:   # tri. 확인
        c[i] -= 3
        tri += 1    # 1하면 두 번째 tri 왔을때 덮어씌우니까 += 1
        continue    # 같은 자리에서 실행을 할게
    if c[i] >= 1 and c[i + 1] >= 1 and c[i + 2] >= 1:        # run 확인
        c[i] -= 1
        c[i + 1] -= 1
        c[i + 2] -= 1
        run += 1
        continue
    # 이 continue들에 안걸리면, 옆 자리 가서 확인
    i += 1

if run + tri == 2:
    print('win')
else: print('lose')

# if문 검색은 줄일수록 좋음!



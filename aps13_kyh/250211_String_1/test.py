n = int(input())        # 길이    ex) 4
t = input()             # 문자열   ex) 8
total = 0
for i in range(8-n+1):          # 회문을 확인하는 구간의 첫 글자 인덱스
    for j in range(n//2):       # 회문의 길이 절반만큼 비교
        if t[i+j] != t[i+n-1-j]:
            break               # 비교 글자가 다르면 현재구간 중지
    else:           # for문이 break에 걸리지 않고 for 종료, 회문이면
        total += 1
print(total)
# n = len(t)
# for i in range(n//2):
#     t[i], t[n-1-i] = t[n-1-i], t[i]
#
# print(t)

# s = "Reverse htis strings"  #sgnirts siht esreveR
# s = s[::-1]
# print(s)

# s1 = 'abc'
# s2 = 'ab'
# s3 = 'def'
# s4 = s2 + 'c'
# print(s1, s4)
# print(s1 == s4)     # 내용 비교
# print(s1 is s4)     # 메모리 주소 비교
# print(s1 is 'abc')

# s1 = 'ab'
# s2 = 'ab'
# s3 = 'ac'
# s4 = 'AC'
# s5 = 'abc'
# print(s1 == s2)
# print(s1 < s2)
# print(s1 < s3)
# print(s3 < s4)
# print(s4 < s5)
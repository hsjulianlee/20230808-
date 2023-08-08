m_1 = 0

list_month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for month in list_month:
   # print("반복 시작")
    #print(f"현재 몇월인가요 -- {month}")
    #print("반복 종료")
    pass
# print(f"for 문 바깥에서 month 변수의 상태 -- {month}")
just_txt = "HelloWorld!"

for txt in just_txt:
    print(txt)

list_month = list(range(1,13))

## while 문

i = 0
while i <= 5:
    print(f"i의 현재 값은.. {i}")
    i += 1

break_cnt = 0
while True:
    if break_cnt > 100:
        break
    print(f"현재 break_cnt 값은 ... {break_cnt}")

    break_cnt += 1

# 연습문제 (1)
print("1부터 10까지의 짝수를 표시합니다.")
for i in range(1,11):
    if i % 2 == 0:
        print(i)

# 연습문제 (2)
print("1부터 10까지의 짝수를 표시합니다.")
for i in range(2,11,2):
    print(i)

# 연습문제 (3)
for i in range(1,10):
    for j in range(1,10):
        print(i*j, end='\t')
    print()

# 연습문제 (4)
for i in range(1,6):
    print(i * '*')

print()
# 연습문제 (5)
for i in range(5,0,-1):
    print(i * '*')

# 별표 그리기

for i in range(10):
    for j in range(15):
        if i == 2 or i + j == 7 or j - i == 7 or i + j == 16 or i - j == 2 or i == 7:
            print("*", end="")
        else:
            print(" ", end="")
    print()

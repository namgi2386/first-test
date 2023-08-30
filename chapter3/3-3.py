t = ['d','e','r']
for i in t:
    print(i)

tr =[(1,2),(3,5),(2,8)]
for (f,g) in tr:
    print(f+g)

marks = [90, 25, 67, 45, 80]   # 학생들의 시험 점수 리스트

number = 0   # 학생에게 붙여 줄 번호
for mark in marks:   # 90, 25, 67, 45, 80을 순서대로 mark에 대입
    number = number +1 
    if mark >= 60: 
        print("%d번 학생은 합격입니다." % number)
    else: 
        print("%d번 학생은 불합격입니다." % number)

print('====================')
number = 0 
for mark in marks: 
    number = number +1 
    if mark < 60:
        continue 
    print("%d번 학생 축하합니다. 합격입니다. " % number)

add = 0
for j in range(1,4) : # 1+2+3
    add = add + j
print(add)

for e in range(2,10):
    for r in range(1,4):
        print(e*r, end=" ")
    print('') 

a = [1,2,3,4]
result = [num*3 for num in a if num % 2 == 0]
print(result)

result2 = []
for num2 in a:
    if num2 %2 == 0:
        result2.append(num2*5)
print(result2)


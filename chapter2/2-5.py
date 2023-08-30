#집합 : set
s1 = set([1,2,3])
s2 = {4,5,6} # 집합
print(s1)
print(s2)
s3 = set("hello")
print(s3) # {'e', 'o', 'l', 'h'} 출력
# 집합에는 순서,중복 없음 , 실행할때마다 다른 순서
#집합자료형은 indexing 할 수 없다
s4 = set([100,200,300])
l4 = list(s4) #집합을 리스트로 변형 후
print(l4[0]) # 리스트 내에서 indexing 출력
t4 = tuple(s4)
print(t4)

s5 = {1,2,3,4,5}
s6 = {7,8,5}
print(s5)
print(s6)
print('=========')
print(s5 & s6) # 교집합
print(s5 | s6) # 합집합
print(s5 - s6) # 차집합
print(s5 ^ s6) # 대칭차집합

s7 = {10,20,30}
s7.add(70) #중복오류
s7.update([100,100,20,200]) #중복제거
print(s7)
s7.remove(10)
print(s7)

l8 = [1,2,2,2,3,4,4,5]
t8 = (6,6,7,7,7,8)
s8 = set(l8)
print(l8) #[]
print(s8) #{}
print(list(s8)) #[]
print(tuple(s8)) #() 

print('\n ========bool=======\n')
x = True
print(x)
y = 1 == 1
print(y)
z = 1 == 2 # 부등호가능 < , >
print(z)
iff = 0 #자료형에 비어있거나, 0 , False , "" 이면 false
iffli = [] #자료형의 값에 따른 속성(true,false)이 존재
if iffli :
    print('굳')
else :
    print('낫굳')

a1 = [1,2,3]
while a1 :
    print(a1)
    a1.pop()
else : 
    print('done')

print(bool(''))

# 변수에 대한 개념 추가
#변수(a) == 주소
#값(1) == 객체 

a2 = [1,2,3]
b2 = a2
c2 = [1,2,3]
print(id(a2))
print(id(b2))
print(a2 is b2)
print(a2 is [1,2,3])
print(a2 is 2527466981888)
print(a2 is c2)
print(id(c2))
print(a2 == c2) 

print("=========")
a3 = [1,2,3]
b3 = a3
a3[0] = 7
print(a3)
print(b3) # same adress same result

print("=========")
a4 = [1,2,3]
b4 = a4[:] #a4 처음부터 끝까지 복사
a4[0] = 7  #슬라이싱하여 가져옴
print(a4)
print(b4) 
b5 = a4.copy()
print(b5)

a6,b6,c6,d6 = '월','화','수','목'
print(c6)
e6 = f6 = '금'

a7,b7 = 3 , 5

temp = a7
a7 = b7
b7 = temp
print(a7) # 다른언어

a8,b8 = 3 , 5
a8,b8 = b8,a8 # in python
print(a8)


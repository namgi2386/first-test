# 튜플은 리스트와 개념적으로 유사하지만
# mutable : 리스트 딕셔너리 집합 : 변경 가능
#immutable : 정수 실수 문자열 튜플 : 변경불가
t1 = () #소괄호로 묶으면 튜플
t2 = (1,) #하나의 변수만 넣으려면 콤마필수
t3 = (1,2,3) #변경하면 안되는 값을 튜플에 담아야함
t4 = 1,2,3
t5 = ('a','b',('ab','cd'))
print(t3[2])

#딕셔너리(사전)
#키(단어)값과 벨류(설명) 값 #Hash map objext JSON

# 유튜브 shift < > 재생속도 m : mute f : full t : theater
dic = {'name':'남기','num':'01023864855','birth':'0928'}
print(type(dic))
dica = {1:'hi'}
print(dica)
dicb = {'a' : ['11','22']}
print(dicb['a'][0])
dicb[10] = 100
print(dicb)
del dic['num']
print(dic)
grade = {'남기' : 'a' , '수연' : 'a+'}
print('남기의 점수는', grade['남기'] ,'입니다')
#    키 중복 불가능   ,     밸류 중복 가능
#    키 정보변경 불가능 : 딕셔너리는 mutable
# so 키는 imutable 자료형을 써야함 

a = '남기'
b = '수연' 
c = '자연'
dicd = {(a,b) : 'mu1' , (c) : 'mu2' , 'name' : 'mu3' }
print('===')
print(type(dicd))
print(dicd)
print(dicd['name'])

#딕셔너리 속 키 는 순서가 존재하지 않는다.

dice = {'name' : '수연' , 'num' : 3437 , 'birth' : '0610' } 
print(dice.keys())
print(list(dice.keys()))

for i in dice.keys() :
    print(i)

print('=====================')
print(dice.values())
print(dice.items()) # [(k,v) , (k,v) , (k,v)]
dicd.clear()
print(dicd)

print('=====================')
print(dice['name'])
print(dice.get('name'))
#print(dice['na'])  :  에러
print(dice.get('na'))  #  : none
print(dice.get('nnnn',"응 안돼"))
print(dice.get('name',"응 안돼"))
print('name' in dice)
print('nameeee' in dice)

print('=====================')
# 리스트와 딕셔너리의 관계
dicf = {0:10 , 1:20 , 2:30}
dicg = (10,20,30)
print(dicf[1])
print(dicg[1]) #결과값이 같다
# 곧 리스트의 값들에게 이름(키)을 부여하는게 딕셔너리이다.

def add(a,b): #매개변수 a,b
    return a+b

print(add(1,4)) #인수 1,4

# 매개변수(parameter)(인자) : 함수에서 정의되어 사용되는 변수 : 점화식속 변수 
# 인수(arguments) : 함수를 호출할 때 건내주는 변수 : 사용(사용자 입력) 변수

def say():
    return 'hi'

ssa = say()
print(ssa)

def ass(a,b):
    print("%d + %d = %d" %(a,b,a+b) )

ak = ass(1,2)
print(ak)


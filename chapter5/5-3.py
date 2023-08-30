# import mod1
# print(mod1.add(4,2))

# from mod1 import add #선택해서 가져오기
# print(add(3,4))

# import mod2
# print(mod2.PI)

# a = mod2.Math()
# print(a.solv(2))

# 예외처리 try: except 오류 as e : else: finally:

# many_error.py
# try:
#     a = [1,2]
#     print(a[3])
#     4/0
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다.")
# except IndexError:
#     print("인덱싱 할 수 없습니다.")

# try_else.py
try:
    age=int(input('나이를 입력하세요: '))
except:
    print('입력이 정확하지 않습니다.')
else:
    if age <= 18:
        print('미성년자는 출입금지입니다.')
    else:
        print('환영합니다.')

abs(-3)
all([1,2,3,0])


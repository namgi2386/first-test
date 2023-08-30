i = 0
while i<3 :
    i += 1
    print("앉아번호 %d번" %i)
    if i == 3:
        print("끝")

print('========')

prompt = '''
1. qwe
2. qwer
3. asd
4. asdf
inprut your answer
'''

'''
number = 0
while number != 4:
    print(prompt)
    number = int(input())'''

#디버깅 F5 , NEXT LINE : F10

coffee = 3
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

a = 0
while a < 10: # Pass는 그냥지나감 continue는 처음으로 돌아감
    a = a + 1 # break는 밖으로나감
    if a % 2 == 0: # ctrl + c 눌러서 반복문 수동탈출(무한실행) 
        continue
    print(a)


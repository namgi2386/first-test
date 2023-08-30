#f = open("doit/새파일.txt", 'w' , encoding="UTF-8")
#f = open("C:/doit/새파일.txt", 'w') #인코딩 : 파일 안깨짐
#f.close()

'''
for i in range(1,11):
    data = "%d번째 \n" % i
    f.write(data)
f.close()
'''

# 새파일2 생성 후 10줄 작성
''' 
f = open("C:\python_namgi\doit\새파일2.txt", 'w' , encoding="UTF-8")
for i in range(1,11):
    data = "%d번째 줄 \n" %i
    f.write(data)
f.close()
'''
f = open("C:/python_namgi/doit/새파일2.txt", 'r' , encoding="UTF-8")
line = f.readline()
print(line)
f.close()



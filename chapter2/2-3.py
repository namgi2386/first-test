odd = [1,2,3,4,5,]
print(type(odd))
a = [1,2,['life','is' ] ]
print(type(odd))
print(a[0]+a[1])
print(a[2])
b = a[2]
print(b[1] + ' ' + b[0] + ' yours? ')

#슬라이싱 
print(odd[::2])
c = [1,2,3]
d = [4,5,6,1]
print(c+d)
print(len(c))
print(str(c[0]) + "hi")
print("hi " *3)
#리스트 수정 삭제
e = [1,2,3]
e[2] = 4
print(e)
del e[1]
print(e)
del(a[:2] ) # a =[ 1,2,['life','is' ] ]
print(a)

#리스트 관련 함수
f = [1,7,3,4,5,'a','c','b']
f.append(4)
f.append('go')
print(f)
g=['a','c','b']
g.sort()
print(g)
g.reverse()
print(g)
print(f , ' ===' ,f.index('go'))
h = [1,2,3,4,5]
h.insert(0,9)
print(h)
h.remove(3)
print(h)
h.pop()
print(h)
h.append([20,30])
print(h)
h.extend([40,50])
print(h)
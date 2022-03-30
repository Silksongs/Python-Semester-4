a = 1
b = 1
c = 300000 # проверено в Python 3.10
d = 300000
print(a is b, c is d)

a, b = 'py', 'py'
c = ''.join(['p', 'y']) # другой объект
print(a is b, a == c, a is c)
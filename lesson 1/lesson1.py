# hello world и переменные

print('hello world')
print('some string')

# переменная a
a = 5
print(a)

# строка в переменной c
c = 'hello py'
print(c)

'''
В python переменные являются указателями 
a -> 5 - выделяется память для числа 5, переменная 'a' указывает на этот участок в памяти
Когда переменные имеют одинаковые значения, они указывают на один участок в памяти
'''

a = 1
b = 2
print(a)
print(b)

temp = a
a = b
b = temp
print(a)
print(b)
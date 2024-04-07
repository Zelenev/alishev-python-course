
# example 1
a = 1
b = 2

if a < b:
    print('a < b')

print('out of block')

# example 2
c = 6
d = 4

if c < d:
    print('c < d')
else:
    print('d < c')

print('out of block 2')

# example 3
e = 8
f = 9

if e < f:
    print('e < f')
elif e == f:
    print('c = f')
else:
    print('f < e')

# example 4
g = 7
h = 8

if g < h:
    print('g < h')
else:
    if g == h:
        print('g == h')
    else:
        print('g > h')

# calculator
name = 'Tom'
height = 2
weight = 80

bmi = weight / (height ** 2)

print('bmi = ' + str(bmi))
if bmi < 25:
    print('у '+name+' нет ожирения')
else:
    print('у '+name+' есть лишний вес')
import math
a = int(input('Задайте a'))
b = int(input('Задайте b'))
h = int(input('Задайте h'))
x = a
s2 = []


while b >= x >=a:
    f = 1 / (math.pow(x, 2) + 1) + math.pow(x, 2)
    s = [f,x]
    print('x=',s[1], 'f(x)=',s[0])
    x=x+h
    s2.append(s)

#s2.sort()
print('Найбільше значення функції', max(s2))

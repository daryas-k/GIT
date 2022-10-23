import math
a = int(input('Задайте a'))
b = int(input('Задайте b'))
c = int(input('Задайте c'))
x = a
s2 = []


while b >= x:
    f = 1 / (math.pow(x, 2) + 1) + math.pow(x, 2)
    s = [f,x]
    print('x=',s[1], 'f(x)=',s[0])
    x=x+c
    s2.append(s)


print('Найбільше значення функції', max(s2))

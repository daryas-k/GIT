import math
a = int(input('Задайте a'))
b = int(input('Задайте b'))
h = int(input('Задайте h'))
x = a

while b >= x >=a:
    f = 1 / (math.pow(x, 2) + 1) + math.pow(x, 2)
    print("x=%.1f y=%.3f"%(x,f))
    x=x+h

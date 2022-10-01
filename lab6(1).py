import math
x = float(input('Задайте x'))
a = int(input('Задайте a'))
b = int(input('Задайте b'))
h = int(input('Задайте h'))



for i in range(a, b, h):
    f = 1 / (math.pow(x, 2) + 1) + math.pow(x, 2)
    print("%i x=%.1f     y=%.3f"%(i,x,f))
    x=x+h

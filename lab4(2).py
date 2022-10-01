import math
def func1(x1,x2,x3,x4):
    W = (6 * x2 - math.sin(x3) + pow(math.cos(x4), 2)) * (math.sqrt(math.fabs(x4))) + math.expm1(x1) / (3 * math.pow(x3, 7))
    return(W)
x=float(input("Введіть х"))
k=float(input("Введіть k"))
a=float(input("Введіть a"))
b=float(input("Введіть b"))
v=func1(x,k,a,b)
print(v)

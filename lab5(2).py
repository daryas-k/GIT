import math
def func1(x1,x2,x3,x4):
    if x1>=math.sqrt(math.pow(x2,2)+math.pow(x3,2)+math.pow(x4,2)):
        w="Точка належить кулі"
    else:
        w="Точка не належить кулі "
    return(w)
D=float(input("Введіть D"))
x=float(input("Введіть x"))
y=float(input("Введіть y"))
z=float(input("Введіть z"))
r=D/2
v=func1(r, x, y, z)
print(v)

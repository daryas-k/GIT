import math
x = float(input('задайте x'))
y = 0.0
if x>=6:
    y = math.pow(3, x-4)+math.log(x, 10)+math.log(x)
elif x>-1 and x<6:
    y=math.pow(x,2)+math.sin(2*x)
elif x<=-1:
    y=2+2.7*math.pow(x,2)
else:
    print('Помилка')
print(y)

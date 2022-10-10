import numpy
import random
n=int(input('Введить N'))
b=int(input('Введить b'))
m=int(input('Введить кількість цифр'))
list2 = []
s=0
while s<m:
    s1=s+1
    c = int(input('Введить число'))
    list2.append(c)
    s=s+1
list1 = []
i=0
while i<n:
    x = random.randint(0, b)
    list1.append(x)
    i = i+1
masiv = numpy.array(list1)
masiv2 = numpy.append(masiv, list2)
masiv2.sort()
print(masiv2)

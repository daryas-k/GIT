from array import *
import numpy as np
import random
n=int(input('Введить N'))
b=int(input('Введить b'))
m=int(input('Введить кількість цифр'))
masiv1 = array('i',[])
s=0
while s<m:
    s1=s+1
    c = int(input('Введить число'))
    masiv1=np.append(masiv1,c)
    s=s+1
masiv = array('i',[])
i=0
while i<n:
    x = random.randint(0, b)
    masiv=np.append(masiv,x)
    i = i+1
masiv2 = np.append(masiv, masiv1)
masiv2.sort()
print(masiv2)

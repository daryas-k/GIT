import numpy as np
import random
i=0
b=12
list=[]
while i<b:
    x=random.randint(1, 24)
    list.append(x)
    i=i+1
masiv = np.array(list)
b = masiv.reshape(3, 4)
print(b)

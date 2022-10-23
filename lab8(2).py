from array import *
import numpy as np
import random
i=0
b=12
masiv = array('i',[])
while i<b:
    x=random.randint(1, 24)
    masiv=np.append(masiv,x)
    i=i+1
if len(masiv)==12:
    b = masiv.reshape(3, 4)
    print(b)

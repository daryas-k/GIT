import math
A=(9,12,8,2)
B=(6,3,9,2)
x=len(A)
c=0
m=0
while c<x:
    s=math.sqrt(math.pow((A[m]-B[m]),2)+math.pow((A[m+1]-B[m+1]),2))
    print(s)
    m=m+2
    c=c+2

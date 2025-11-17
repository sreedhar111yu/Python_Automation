import math


n =6

i =math.sqrt(n)
while i>0:
    a=n//i
    b=n+a

print(abs(b-n))
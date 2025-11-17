n =15
m= 6

q =n//m
r =n%m

A= q*m
B= (q+1)*m

C = abs(n-A)
D= abs(n-B)
if C<D:
    n=abs(n-C)
elif C==D:
    n=n+D
else:
    n=abs(n+D)

print(q)
print(r,A,B,C,D,n)
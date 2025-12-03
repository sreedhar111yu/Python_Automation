def prime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if(n%i == 0):
            return False
    
    return True
sum = 0
for n in range(10,100):
    if(prime(n)):
        sum=sum+n
print(sum)
    
def prime(n):
    for i in range(2, int(n**0.5)+1):
        if(n % i == 0):
            return False
    
    return True

sum =0
for i in range(1,10):
    if(prime(i)):
        sum+=i
print(sum)
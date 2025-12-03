def is_prime(n):

    if n < 2:
        return False
    for i in range(2,int(n**0.5) +1):
         if(n % i == 0):
             return False
    
    return True

cnt =0
for num in range(100, 1000):
    if is_prime(num):
        cnt+=1
print(cnt)
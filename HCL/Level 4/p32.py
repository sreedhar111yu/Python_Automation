def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if(n%i == 0):
            return False
        
    return True
sum = 0
for num in range(2,10000):
    if(is_prime(num)):
        temp = num
        sum =0

        while temp > 0:
            sum += temp%10
            temp = temp // 10
        if(sum == 14):
            print(num)
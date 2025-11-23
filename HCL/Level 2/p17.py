def prime(x):
    is_prime = True
    for i in range(2,x):
        if(x % i == 0):
            is_prime = False
            break
    
   
    if(is_prime):
        print("Prime")
    else:
        print(" not prime")
    sum =0
    temp =x
    while temp >0:
        sum += temp % 10
        temp = temp // 10
    
    if(sum == 14):
        print("sum of dig is 14")
    else:
        print("sum of digits is not 14")
    

def main():
    x = int(input("enter x : "))
    prime(x)

main()     

# enter x : 59
# Prime
# sum of dig is 14

# enter x : 77
#  not prime
# sum of dig is 14

# enter x : 13
# Prime
# sum of digits is not 14
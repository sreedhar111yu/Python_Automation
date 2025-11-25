def prime(x):
    is_prime =True

    for i in range(2,x):
        if(x % i == 0):
            is_prime =False
    
    return is_prime
pass



def main():
    x = int(input("enter x : "))
    res = prime(x)

    if(res):
        print(f"{x} is prime number")
    else:
        print(f"{x} is not a prime number ")
main()
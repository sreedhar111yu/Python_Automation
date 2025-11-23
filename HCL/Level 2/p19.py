def prime(n):
    for i in range(2,n):
        if(n%i == 0):
            print("not a prime")
            break
    
    else:
        print("prime")


def main():
    x = int(input("enter a num : "))
    h = (x // 100) % 10
    ten = (x // 10) % 10
    p = h * 10 + ten
    prime(p)
    print(p)

main()

"""
enter a num : 3517
not prime
51

enter a num : 6359
not prime

"""
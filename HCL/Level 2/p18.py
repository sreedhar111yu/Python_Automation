def prime(n):
    for i in range(2,n):
        if(n%i == 0):
            print("not a prime")
            break
    
    else:
        print("prime")


def main():
    x = int(input("enter x :"))
    q = x %100
    prime(q)

main()

'''
enter x :359
prime

enter x :3577
not a prime
'''
def rev():
    x = int(input("Enter a four dig no. : "))
    loop = 2 
    rev =0

    while loop > 0:
        rem = x % 10
        rev = rem + rev * 10
        x = x // 10
        loop = loop - 1 
    
    x  = x * 100
    y  = x + rev

    print(f"res : {y}")

rev()


# Enter a four dig no. : 3895
# res : 3859
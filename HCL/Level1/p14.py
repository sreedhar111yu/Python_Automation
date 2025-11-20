def rev_of_dig():
    x = int(input("enter three dig no : "))
    rev =0

    while x > 0:
        rem = x % 10
        rev = rem + rev*10
        x = x // 10

    print(f"res : {rev}")

rev_of_dig()


# enter three dig no : 123
# res : 321
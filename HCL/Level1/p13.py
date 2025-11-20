def rev_of_dig():
    x = int(input("enter two dig no : "))
    rev =0

    while x > 0:
        rem = x % 10
        rev = rem + rev*10
        x = x // 10

    print(f"res : {rev}")

rev_of_dig()


# enter two dig no : 45
# res : 54
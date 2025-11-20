def sum_of_dig():

    x = int(input("Enter two dig no : "))
    rem = x % 10
    q = x // 10
    y = rem + q

    print(f"res : {y}")
sum_of_dig()

# Enter two dig no : 69
# res : 15
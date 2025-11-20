def sum_of_dig():
    x = int(input("Enter three dig no : "))
    sum =0

    while x > 0:
        rem = x % 10
        sum = rem + sum
        x = x // 10

    print(f" res : {sum}")

sum_of_dig()


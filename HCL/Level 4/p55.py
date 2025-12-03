def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a // b   # if you want integer division

def main():
    while True:
        print("ENTER THE OPTION FROM BELOW")
        print("1 - ADD")
        print("2 - SUB")
        print("3 - MULTI")
        print("4 - DIV")
        print("5 - EXIT")

        option = int(input("Enter option: "))

        if option == 5:
            break

        a = int(input("Enter a: "))
        b = int(input("Enter b: "))

        if option == 1:
            print("Result:", addition(a, b))
        elif option == 2:
            print("Result:", subtraction(a, b))
        elif option == 3:
            print("Result:", multiplication(a, b))
        elif option == 4:
            print("Result:", division(a, b))
        else:
            print("Invalid option")

main()

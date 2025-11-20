def main():
    x = int(input("enter a four dig no : "))

    hundreds = (x // 100) % 10
    tens = (x // 10) % 10

    res = x - 5 * (hundreds == tens)
    print("res :", res)

main()

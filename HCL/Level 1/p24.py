def main():
    x = int(input("enter three dig no : "))
    rem = x  % 10
    q = x // 100

    res = x - 5 *(rem == q)
    print(f"res : {res}")

main()

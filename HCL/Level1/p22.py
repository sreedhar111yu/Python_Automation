def main ():
    x = int(input("enter val : "))
    mid = (x // 10) % 10

    res = x - 5 *(mid % 2 )
    print(f"res : {res}")

    

main()
def main():

    x = int(input("enter  three dig_num : "))
    rem = x % 10
    q = x // 100

    y = (q * 100) + rem
    print(f"res : {y} ")

main()
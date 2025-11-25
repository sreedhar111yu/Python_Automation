def ascending(x):
    prev = 10

    while x > 0:
        curr = x % 10
        if curr >= prev:
            return False
        prev = curr
        x //= 10   
    return True


def main():
    x = int(input("enter x : "))
    if ascending(x):
        print("YES")
    else:
        print("False")

main()

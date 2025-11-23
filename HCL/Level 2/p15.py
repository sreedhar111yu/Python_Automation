def main():
    x = int(input("enter a num : "))
    s = str(x)

    first_dig = int(s[0])

    if first_dig % 2 == 0:
        print(x)
        return

    # first digit is odd → reduce it by 1
    new_first = first_dig - 1

    # build new string 
    res_str = str(new_first) + s[1:]

    # convert back to int
    res = int(res_str)

    print(res)

main()

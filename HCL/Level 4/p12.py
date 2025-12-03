def reverse(x):
    rev =0
    while x > 0:
        rem = x % 10
        rev = rem+rev*10
        x = x // 10
    return rev

def main():
    x = int(input("enter x :"))
    res = reverse(x)
    print(res)
main()
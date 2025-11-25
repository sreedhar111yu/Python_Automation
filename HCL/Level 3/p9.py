def swap_dig(x):
    a = x // 10
    b = x % 10
    temp = a
    a = b
    b = temp

    dig = a * 10 + b
    return dig

def main():
    x = int(input("enter x :"))
    res = swap_dig(x)
    print(res)

main()

# enter x :34
# 43
def count_dig(x):
    cnt =0

    while x > 0:
        cnt+=1
        x = x //10
    return cnt

def main():
    x = int(input("enter x :"))
    res = count_dig(x)
    print(res)
main()
123

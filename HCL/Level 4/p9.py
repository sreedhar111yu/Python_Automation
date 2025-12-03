def sum_of_dig(x):
    sum = 0
    while x >0:
        sum+= x % 10
        x = x // 10
    return sum
def main():
    x = int(input("enter x : "))
    res = sum_of_dig(x)
    print(res)
main()
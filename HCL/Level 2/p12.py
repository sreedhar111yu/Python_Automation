def main():
    x = int(input("enter num : "))
    sum =0

    while x > 0:
        sum += x % 10
        x = x // 10
    print (sum)
main()

# enter num : 123456
# 21

# enter num : 675
# 18
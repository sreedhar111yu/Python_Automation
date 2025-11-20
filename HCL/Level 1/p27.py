def main():
    x = int(input("enter a three dig no : "))
    sum =0

    while x > 0:
        rem = x % 10
        sum = rem + sum
        x = x // 10

    if(sum == 10):
        print("SUCCESS")
    else:
        print("FAILURE")

main()

# enter a three dig no : 127
# SUCCESS

# enter a three dig no : 956
# FAILURE
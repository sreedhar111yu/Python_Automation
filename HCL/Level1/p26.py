def main():

    x = int(input("enter a two dig no : "))
    sum =0
    while x > 0:
        rem = x % 10
        sum = rem + sum
        x = x//10

    if(sum == 10):
        print("SUCCESS")
    else:
        print("FAILURE")

main()

# enter a two dig no : 56
# FAILURE

# enter a two dig no : 37
# SUCCESS
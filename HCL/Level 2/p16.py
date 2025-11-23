def main():
    x = int(input("enter a num : "))

    for i in range(2, x):
        if x % i == 0:
            print("Not a prime")
            break
    else:
        print("Prime")

main()

# enter a num : 31
# Prime

# enter a num : 27
# Not a prime
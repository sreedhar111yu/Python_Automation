def main():

    x = int(input("enter three dig no : "))
    sum =0
    loop = 2

    while loop > 0:
        rem = x % 10
        sum = rem + sum
        loop= loop -1
        x  = x // 10

    if(sum <= 10 ):
        print("SUCCESS")
    else:
        print("FAILURE")

    print(sum)

main()

# enter three dig no : 569
# FAILURE
# 15

# enter three dig no : 316
# SUCCESS
# 7
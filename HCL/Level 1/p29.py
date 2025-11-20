def main():
    x = int(input("enter  4 dig no : "))

    hundreds  = (x // 100 ) % 10
    tens = (x // 10) % 10
    sum = hundreds + tens
    if(sum > 10):
        print("SUCCESS")
    else:
        print("FAILURE")

    print(hundreds, tens, sum)

main()

# enter  4 dig no : 7529
# FAILURE
# 5 2 7

# enter  4 dig no : 9386
# SUCCESS
# 3 8 11
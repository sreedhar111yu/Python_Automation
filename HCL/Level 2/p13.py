def main():

    x  = int(input("enter num : "))
    rev=0

    while(x > 0):
        rem = x % 10
        rev = rem+rev*10
        x = x // 10
    
    print(rev)
main()

# enter num : 123456
# 654321
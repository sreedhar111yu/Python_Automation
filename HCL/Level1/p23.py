def main():

    x = int(input("enter a num : "))
    i = x
    sum =0
    while (x > 0):
        rem = x % 10
        sum = rem + sum
        x =  x // 10

    res = (i - 5 *(sum % 2 ))
    print(f"res : {res}")
    
main()


# enter a num : 72
# res : 67

# enter a num : 95
# res : 95
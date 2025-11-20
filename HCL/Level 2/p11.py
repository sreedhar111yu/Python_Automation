def main():
    x = int(input("enter x num :"))
    cnt =0
    while x > 0:
        x = x //10
        cnt+=1
    
    print(cnt)
main()

# enter x num :123456
# 6
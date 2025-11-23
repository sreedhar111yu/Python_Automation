def main():
    x = int(input("enter x :"))
    cnt=0

    while x> 0:
        last_dig = x % 10
        if(last_dig in (2,3,5,7)):
            cnt+=1
        
        x =x//10
    print(cnt)

main()
# enter x :163496481
# 1
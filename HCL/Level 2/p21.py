def main():
    x = int(input("enter x : "))
    sum =0

    while(x > 0):
        rem = x % 10
        if(rem % 2 != 0):
            sum+=1
        
        x = x//10
    
    print(sum)
main()
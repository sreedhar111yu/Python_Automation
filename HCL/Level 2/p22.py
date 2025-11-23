def main():
    x = input(("enter x :")).strip()

    cnt =0
    for i in range(len(x)-1):

        pair = x[i:i+2]

        first_dig =pair[0]
        last_dig = pair[1]
        if(first_dig != '0') and int(last_dig) % 2 == 1:
            cnt+=1
    

    print(cnt)
main()

# enter x :12345678
# 3
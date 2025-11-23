def main():
    cnt =0
    for i in range(2,10):
        if (i > 1):
            for j in range(2,i):
                if(i%j == 0):
                    break
            else:
                cnt+=1
    
    print(cnt)

main()

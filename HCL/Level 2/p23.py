import math
def main():

    x = int(input("enter a num : "))
    cnt =0

    while x > 0:
        rem = x % 10
        root = math.sqrt(rem)
        if(root*root == rem):
            cnt+=1

        x = x//10


    print(cnt)

main()
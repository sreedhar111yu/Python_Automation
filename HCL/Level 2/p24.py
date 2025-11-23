import math
def main():
    x = input("enter x :").strip()
    cnt =0

    for i in range(len(x)-1):
        pair = int(x[i:i+2])

        root =int(math.sqrt(pair))
        if(root*root == pair):
            cnt+=1
    
    print(cnt)
main()
# enter x :163496481
# 4
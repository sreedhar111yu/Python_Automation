def array(a,n):
    res = [0]*(n+1)
    carry = 0
    for i in range(n-1,-1,-1):
        s = a[i]+carry
        res[i+1] = s % 10
        carry  = s // 10
    
    return res



def main():
    n = int(input("enter size : "))
    a = list(map(int, input("Enter A :").split()))
    
   
    res = array(a,n)
    print(f"res : {res}")

main()
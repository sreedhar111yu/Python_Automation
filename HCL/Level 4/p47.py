def array(a,b,n):
    res = [0]*(n+1)
    carry =0
    for i in range(n-1,-1,-1):
        s = a[i]+b[i]+carry
        res[i+1] = s % 10
        carry = s // 10

    res[0] = carry
    return res

def main():
    n = int(input("enter size : "))
    a = list(map(int, input("Enter A :").split()))
    
    b = list(map(int, input("Enter B: ").split()))

    res = array(a,b,n)
    print(f"res : {res}")

main()
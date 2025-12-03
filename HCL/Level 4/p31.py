def find_zeros(x):
    cnt=0
    while x > 0:
        rem = x % 10
        if(rem == 0):
            cnt+=1
        x = x // 10
    return cnt
def main():
    res =0
    for i in range(1,10001):
        res += find_zeros(i)
    print(res+1)
main()
        # 2894
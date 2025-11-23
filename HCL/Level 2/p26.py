import math
def main():
    x = 9999
    a =7
    b =9
    hcf = math.gcd(a,b)
    lcm = (a*b)//hcf
    res = (x//lcm)*lcm
    print(res)

main()

# 9954
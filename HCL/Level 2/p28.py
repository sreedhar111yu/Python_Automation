import math
def main():
    a = int(input("a : "))
    b = int(input("b : "))

    hcf = math.gcd(a,b)
    lcm = (a*b)//hcf

    print(lcm)
main()
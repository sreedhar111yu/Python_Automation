import math

def lcm(x, y):
    return x * y // math.gcd(x, y)

def main():
    a = int(input("a : "))
    b = int(input("b : "))
    c = int(input("c : "))

    result = lcm(lcm(a, b), c)
    print(result)

main()

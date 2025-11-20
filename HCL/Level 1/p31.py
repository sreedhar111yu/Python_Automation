def sum(x):
    s =0
    while x > 0:
        rem = x %10
        s = s + rem
        x = x //10

    return s

def main():
    x = int(input("Enter three dig_input : "))
    res = sum(x)
    while res >= 10:
        res = sum(res)
    
    print(res)
   

main()
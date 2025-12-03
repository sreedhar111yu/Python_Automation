def is_pal(x):
    rev =0
    n = x

    while x > 0:
        rem = x % 10
        rev = rem+rev*10
        x = x // 10
    
    return rev == n

def main():
    for i in range(1, 100000):
        if(is_pal(i)):
            print(i)
main()



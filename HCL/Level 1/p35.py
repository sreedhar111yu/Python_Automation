

def bigger_sum(x,y):
    hun_x,tens_x,ones_x = (x // 100)%10,(x//10) %10, x%10
    hun_y,tens_y, ones_y = (y // 100)%10,(y//10)%10, y%10

    sum_x = hun_x + ones_x
    sum_y = hun_y + ones_y
    if(sum_x > sum_y):
        tol_sum = hun_x +tens_x+ones_x
    else:
        tol_sum =hun_y +tens_y+ones_y

    return tol_sum


def main():
    x =int(input("enter 3 dig no : "))
    y =int(input("enter 3 dig no y : "))

    res = bigger_sum(x, y)
    print(res)

main()

# enter 3 dig no : 856
# enter 3 dig no y : 978
# 24

# enter 3 dig no : 128
# enter 3 dig no y : 365
# 11
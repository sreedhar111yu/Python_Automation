def diff(x,y):
   
    hun_x, tens_x, ones_x = (x//100)%10, (x //10)%10, x %10
    hun_y, tens_y, ones_y = (y//100)%10, (y //10)%10, y %10

    if(tens_x > tens_y):
        c_h = hun_x
        c_o = ones_x
    else:
        c_h = hun_y
        c_o = ones_y
    
    diff = abs(c_h - c_o)
    return diff


def main():
    x = int(input("enter a 3_dig no x: "))
    y = int(input("enter a 3_dig no y: "))

    res = diff(x ,y)
    print(res)
main()

# enter a 3_dig no x: 128
# enter a 3_dig no y: 365
# 2
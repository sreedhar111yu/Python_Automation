def sum_of_dig(x,y):
    dig =2
    sum_x= 0
    sum_y = 0
    while dig > 0:
        sum_x += x % 10
        sum_y += y % 10
        
        x = x // 10
        y = y // 10
        dig = dig -1

    return max(sum_x,sum_y)



def main():
    x = int(input("enter two dig no x :"))
    y = int(input("enter two dig no y :"))
    res =sum_of_dig(x,y)
    print(res)
main() 

# enter two dig no x :56
# enter two dig no y :78
# 15

# enter two dig no x :14
# enter two dig no y :65
# 11
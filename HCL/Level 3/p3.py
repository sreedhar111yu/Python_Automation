def sum14(no):
    # while no > 0:
    #     sum_of_dig += no%10
    #     no=no//10
    
    sum_of_dig = sum(int(digit) for digit in str(no))
    if(sum_of_dig == 14):
        return 1
    else:
        return 0
    
def main():
    number = int(input("enter num : "))
    res = sum14(number)
    if(res == 1):
        print("sum of digit is 14")
    else:
        print("sum of digit not 14")
main()

"""
enter num : 59
sum of digit is 14

enter num : 123
sum of digit not 14
"""
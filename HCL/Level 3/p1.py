def function(no1):
    no2 =0

    no2 = no1 + 2

    return no2

def main():
    number1 = int(input("enter a num : "))
    number2 = function(number1)
    print(number2)
main()

"""
enter a num : 45
47

enter a num : 56789
56791
"""
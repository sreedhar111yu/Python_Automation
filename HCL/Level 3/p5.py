def find_number_of_zeros(number):
    cnt=0

    while number>0:
        rem = number % 10
        if(rem == 0):
            cnt+=1
        
        number = number//10
    
    return cnt
def main():
    x = int(input("enter x : "))
    res = find_number_of_zeros(x)
    print(res)
main()


"""
enter x : 100
2

enter x : 1060030
4
"""
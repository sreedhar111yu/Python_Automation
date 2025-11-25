def compare(a,b):
    if(a == b):
        return 1
    else:
        return 0
    
def main():
    a = int(input("enter a : "))
    b = int(input("enter b : "))
    res =compare(a,b)
    if(res):
        print("Same")
    else:
        print("not same")

main()

"""
enter a : 123
enter b : 123
Same
enter a : 56789
enter b : 12345
not same
"""
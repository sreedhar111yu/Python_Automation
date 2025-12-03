def addition(a,b):
    pass

def subtraction(a,b):
    pass

def multipication(a,b):
    pass

def division(a,b):
    pass


def switch_case(o):
    switch = {
        1:addition(),
        2:subtraction(),
        3:multipication(),
        4:division()
    }
def main():
    a = int(input("enter a : "))
    b = int(input("enter b : "))
    o = int(input("enter  1 for Add, 2 for Sub,3 for Multi, 4 for Div,5 Exit  enter your choice"))
    switch_case(o)
    add = addition(a,b)
    print(add)
    sub = subtraction()
    print(sub)
    multi = multipication()
    print(multi)
    div = division()
    print(div)

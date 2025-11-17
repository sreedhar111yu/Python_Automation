# Enclosing variable

def card():
    discount =10

    def checkout():
        print("your total discount is :",discount)

    checkout()
card()
class employee:
    def __init__(self,fname,lname):  #constructor
        self.first_name =fname
        self.last_name=lname

    def profile(self):
        print(f"Full name in profile:{self.first_name}{self.last_name}")
    
    def bank(self):
        print(f"Full name in bank:{self.first_name}{self.last_name}")

s1=employee('Sreedhar','V')
s1.profile()
s1.bank()
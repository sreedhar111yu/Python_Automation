'''Create a class MaxFinder that identifies the largest number in a list.'''
class MAx_finder:
    def __init__(self,number):
        self.number =number
    def find(self):
        a =max(self.number)
        print(f"largest number in list is :{a}")
    
f=MAx_finder([1, 5 , 9 ,3, 6])
f.find()
        
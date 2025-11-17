class mathapp:
    def __init__(self,n):
        self.square =n
        self.cube =n

    def Square(self):
       A= self.square*self.square
       print(A)

    def cb(self):
       print(self.cube*self.cube*self.cube)
       

s1 = mathapp(4)
s1.Square()
s1.cb()

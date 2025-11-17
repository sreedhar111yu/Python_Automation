class student:
    def __init__(self,name,grade):  #CONSTRUCTOR
        self.name = name
        self.grade = grade

    def display(self):
        print(f"{self.name} and {self.grade}")


# multi object creation for same class 
s1= student('sreedhar',74)
s2 = student('swetha',90)
s3 = student('abai',85)

s1.display()
s2.display()
s3.display()


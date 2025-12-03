class student:
    def __init__(self,Student_id, Math_Mark, Science_Mark):
        self.Student_id = Student_id
        self.Math_Mark = Math_Mark
        self.Science_Mark = Science_Mark
        self.pointer = None
class student_linkedlist:
    def __init__(self):
        self.head =None
    
    def add(self,Student_id,Math_Mark,Scince_Mark):
        newNode = student(Student_id,Math_Mark,Scince_Mark)
        
        if(self.head is None):
            self.head = newNode
        else:
            curr = self.head
            while(curr.pointer is not None):
                curr = curr.pointer
            curr.pointer= newNode
    
    def display(self):
        if self.head is None:
            print("no Student rec found")
            return
        
        curr = self.head
        while curr is not None:
            print(f"ID:{curr.Student_id},Math Mark:{curr.Math_Mark},Science Mark:{curr.Science_Mark}")
            curr= curr.pointer
def main():

    A = student_linkedlist()
    print("Enter a student rec...")

    while True:
        try:
            Std_id = int(input("Enter Student ID : "))
        except ValueError:
            print("Invalid Input ")
            continue
        if(Std_id == -1):
            break

        try:
            math = int(input("Enter Math Mark"))
            science= int(input("Enter Math Mark"))
        except ValueError:
            print("Invalid Inputs ")
            continue
        A.add(Std_id,math,science)
        print("Record added. \n")
        A.display()
main()

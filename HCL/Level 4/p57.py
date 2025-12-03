class student:
    def __init__(self,student_id,math_mark,science_mark):
        self.student_id = student_id
        self.math_mark = math_mark
        self.science_mark = science_mark
        self.pointer = None
class student_linledlist:
    def __init__(self):
        self.head = None

    def add(self,student_id,math_mark,science_mark):
        newNode = student(student_id,math_mark,science_mark)
        if(self.head is None):
            self.head = newNode
        else:
            curr = self.head
            while(curr.pointer is not None):
                curr = curr.pointer
            curr.pointer = newNode
    # DISPLAY FUNCTION
    def display(self):
        if(self.head is None):
            print("No Recoard found")
            return
        
        curr = self.head
        while(curr is not None):
            print(f"ID: {curr.student_id}\n Math Mark :{curr.math_mark}\nScience Mark: {curr.science_mark}")
            curr = curr.pointer

        # INSERT OPREATION HEAD NODE
    def insert_before(self,traget_id:int, student_id:int,math_mark:int,science_mark:int):
        newNode = student(student_id,math_mark,science_mark)
        if(self.head is None):
            print("Node Head has empty elements")
            return
        if(self.head.student_id == traget_id):
            newNode.pointer = self.head
            self.head = newNode
            return
        
        #INSERT OPERATION PREV NODE

        prev = None
        curr = self.head
        while(curr is not None and curr.student_id != traget_id):
            prev = curr
            curr = curr.pointer
        if(curr is None):
            print("Target is Not Found")
            return
        
        prev.pointer = newNode
        newNode.pointer = curr
    #INSERT AFTER NODE
    def insert_after(self,traget_id:int,student_id:int,math_mark:int,sicence_mark):
        newNode = student(student_id,math_mark,sicence_mark)

        curr = self.head
        while(curr.pointer is not None and curr.student_id != traget_id):
            curr = curr.pointer

        if(curr is None):
            print("Traget Id is Not Found")
            return

        newNode.pointer=curr.pointer
        curr.pointer = newNode




A = student_linledlist()
A.add(1,90,56)
A.add(2,88,555)
A.add(3,74,56)
A.add(4,28,63)
A.display()
A.insert_before(3,7,99,96)
A.display()
A.insert_after(3,8,88,99)
A.display()
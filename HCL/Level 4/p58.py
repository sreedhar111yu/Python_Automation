class student:
    def __init__(self,student_id,maths_mark,science_mark):
        self.student_id = student_id
        self.maths_mark = maths_mark
        self.sicence_mark = science_mark
        self.next = None
        pass
class studentLinkedlist:
    def __init__(self):
        self.head = None
        pass

    def add(self,student_id,maths_mark,science_mark):
        newNode = student(student_id,maths_mark,science_mark)
        if(self.head is None):
            self.head = newNode
        else:
            curr = self.head
            while(curr.next is not None):
                curr = curr.next
            curr.next = newNode
        pass

    def display(self):
        if(self.head is None):
            print("NO Records Found")
            return
        
        curr = self.head
        while curr is not None:
            print(f"ID:{curr.student_id} \n Math : {curr.maths_mark} \n Science:{curr.sicence_mark}")
            curr=curr.next

        pass
    def insert_before(self,traget_id:int,student_id:int,maths_mark:int,science_mark:int):
        newNode = student(student_id,maths_mark,science_mark)

        if(self.head is None):
            print("Node is Empty or no data")
            return
        if(self.head.student_id == traget_id):
            newNode.next = self.head
            self.head = newNode
            return
        
        prev = None
        curr = self.head
        while(curr is not None and curr.student_id != traget_id):
            prev = curr
            curr=curr.next
        
        if(curr is None):
            print("traget is not found ")
            return
        prev.next = newNode
        newNode.next = curr
    
    def insert_after(self,traget_id:int,student_id:int,math_mark:int,science_mark:int):
        newNode = student(student_id,math_mark,science_mark)

        curr = self.head
        while(curr is not None and curr.student_id != traget_id):
            curr = curr.next
        if(curr is  None):
            print("Traget id not Found")
            return
        newNode.next = curr.next
        curr.next = newNode
        pass
    def delete(self,traget_id:int):
        if(self.head is not None):
            if(self.head.student_id == traget_id):
                self.head =self.head.next
                return
            
            curr = self.head
            prev = None
            while(curr is not None and curr.student_id != traget_id):
                prev = curr
                curr = curr.next
            if(curr is None):
                print("Traget not found")
                return
            prev.next =curr.next
            

        else:
            print("Head node in empty")
        pass

A= studentLinkedlist()
A.add(1,80,96)
A.add(2,60,96)
A.add(3,70,56)
A.display()
A.insert_before(3,5,55,50)
A.display()
A.insert_after(3,9,54,39)
A.display()
A.delete(2)
A.display()


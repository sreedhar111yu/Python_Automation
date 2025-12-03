"""
class AdmissionForm:
    Name =  None
    Age = None
    Gender = None
    Address = None
    def __init__(self,Name,Age,Gender,Adderess):
         self.Name = Name
         self.age = Age
         self.gender = Gender
         self.adderess = Adderess

xerox1 = AdmissionForm("abc",20,"male","chennai")

print(xerox1.Name)
"""
#-------------------------------------------------------------------------------------------------
"""class Node:
    data = None
    pointer = None
    def __init__(self,data):
        self.data=data
   # creating Node 
node1 = Node(10)
node2 = Node("Hello")
print(node1.data)
print(node1.pointer)
print(node2.data)
"""

#------------------------------------------------------------------------------------------------       
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.pointer = None

head = Node(1)
node2 = Node(2)
node3 = Node(3)

head.pointer = node2
node2.pointer = node3

curr = head

while(curr is not None):
    print(curr.data)
    curr = curr.pointer
        
"""
#-------------------------------------------------------------------------------------------------------
class Node:
    def __init__(self,data):
        self.data = data
        self.pointer = None
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self,data):
        newNode = Node(data)
        if(self.head is None):
            self.head = newNode
        else:
            curr = self.head

            while curr.pointer  is not None:
                curr = curr.pointer
            curr.pointer = newNode
    def print(self):
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.pointer

    def remove(self,data):
        if self.head is not None:
            if(self.head.data == data):
                self.head = self.head.pointer
            else:
                curr = self.head
                while (curr.pointer is not None and curr.pointer.data != data):
                    curr = curr.pointer
                curr.pointer= curr.pointer.pointer
        else:
            print("head node is empty")
            

a = LinkedList()
a.add(1)
a.add(2)
a.add(3)
a.add(4)
a.print()
a.remove(3)
a.print()
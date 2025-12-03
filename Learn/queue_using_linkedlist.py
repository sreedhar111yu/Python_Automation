class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        pass
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        pass
    def insert(self, data):
        newNode = Node(data)
        if(self.front is None ):
            self.front = newNode
            self.rear = newNode
            return
        self.rear.next = newNode
        self.rear = newNode
    def delete(self,data):
        if(self.front is None):
            print("Queue is empty")
            return
        if(self.front == self.rear):
            self.front = None
            return
        curr = self.front
        self.front = self.front.next
        curr.next = None
        curr = None
    
    def display(self):
        if(self.front is None):
            print("queue is empty")
        
        curr = self.front
        while curr:
            print(curr.data)
            curr = curr.next
    


A = Queue()
A.insert(1)
A.insert(2)
A.insert(3)
A.insert(4)
A.display()
A.delete(1)
A.display()
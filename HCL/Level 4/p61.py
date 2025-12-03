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

    def insert(self):
        data = int(input("enter element to be into queue : "))
        newNode = Node(data)
        if(self.front is None):
            self.front = newNode
            self.rear = newNode
            return
        self.rear.next = newNode
        self.rear = newNode
    def delete(self):
        if(self.front is None):
            print("queue is empty")
        elif self.front.next is None:
            print("popped element is : ",self.front.data)
            print("------------------------------------")
            self.front=None
        else:
            curr = self.front
            print("popped element is : ",self.front.data)
            print("------------------------------------")
            self.front = curr.next
            curr = None
        pass
    def display(self):
        if(self.front is None):
            print("Queue is empty")
            return
        print("Elements of Queue are : ")
        curr = self.front
        while curr:
            print(curr.data)
            curr =  curr.next
        print("front of Queue is : ", self.front.data)
        print(f"Rare of  queue is {self.rear.data}")
        
        pass

Q = Queue()

while(1):
    print("ENTER THE OPTION FROM BELOW")
    print("1-PUSH OPERATION \n2-POP OPERATION \n3-DISPLAY\n4-EXIT")
    option =  int(input())
    if(option == 1):
        print("PUSH OPERATION")
        print("--------------")
        Q.insert()
    elif option == 2:
        print("POP OPERATION")
        print("--------------")
        Q.delete()
    elif option == 3:
        print("DISPLAY")
        print("---------------")
        Q.display()
    else:
        break
"""
ENTER THE OPTION FROM BELOW
1-PUSH OPERATION
2-POP OPERATION
3-DISPLAY
4-EXIT

25
26
27
28
29
30
front of Queue is :  25

popped element is :  25
"""

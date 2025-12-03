class Node:
    def __init__(self,x):
        self.data = x
        self.next = None
        pass
class Stack:
    def __init__(self):
        self.top = None
        pass

    def push(self):
        x = int(input("enter element to be inserted into stack"))
        newNode = Node(x)
        if self.top is None:
            self.top = newNode
            return
        newNode.next = self.top
        self.top = newNode
    
    def pop(self):
        if self.top is None:
            print("Stack is empty")
        elif self.top .next is None :
            print(f"poped element is : {self.top.data}")
            print("-----------------------------")
            self.top =None
        else:
            curr = self.top
            self.top = curr.next
            curr = None
        
    def display(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("element of stack")
            curr = self.top
            while curr:
                print(curr.data)
                curr =curr.next
      
s = Stack()

while(1):
    print("ENTER THE OPTION FROM BELOW")
    print("1-PUSH OPERATION \n2-POP OPERATION \n3-DISPLAY\n4-EXIT")
    option =  int(input())
    if(option == 1):
        print("PUSH OPERATION")
        print("--------------")
        s.push()
    elif option == 2:
        print("POP OPERATION")
        print("--------------")
        s.pop()
    elif option == 3:
        print("DISPLAY")
        print("---------------")
        s.display()
    else:
        break

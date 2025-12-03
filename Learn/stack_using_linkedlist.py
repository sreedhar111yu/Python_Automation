class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.top
        self.top = newNode

    def pop(self):
        if self.top is None:
            print("Stack is empty")
            return

        value = self.top.data
        self.top = self.top.next
        return value

    def display(self):
        if self.top is None:
            print("Stack empty")
            return

        curr = self.top
        while curr:
            print(curr.data)
            curr = curr.next
s = Stack()

print("=== PUSH ===")
s.push(10)
s.push(20)
s.push(30)
s.display()

print("\n=== POP ===")
print("Popped:", s.pop())
s.display()

print("\n=== POP AGAIN ===")
print("Popped:", s.pop())
s.display()

print("\n=== POP ALL ===")
print("Popped:", s.pop())
s.pop()   # empty pop
s.display()

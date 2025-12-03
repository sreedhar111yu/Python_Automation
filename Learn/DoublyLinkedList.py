class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedlist:
    def __init__(self):
        self.head = None

    def add_to_end(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return

        curr = self.head
        while curr.next is not None:
            curr = curr.next

        curr.next = newNode
        newNode.prev = curr

    def add_to_start(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return

        self.head.prev = newNode
        newNode.next = self.head
        self.head = newNode

    def delete(self, data):
        if self.head is None:
            print("List is empty")
            return

        # delete head
        if self.head.data == data:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            return

        curr = self.head

        # search
        while curr is not None and curr.data != data:
            curr = curr.next

        if curr is None:
            print("Value not found")
            return

        # delete middle
        if curr.next is not None:
            curr.next.prev = curr.prev

        # delete last
        if curr.prev is not None:
            curr.prev.next = curr.next

    def display(self):
        if self.head is None:
            print("no records found")
            return
        curr = self.head
        while curr is not None:
            print(f"data : {curr.data}")
            curr = curr.next


# Doubly Linked List Testing

A = DoublyLinkedlist()

print("=== Initial add_to_end ===")
A.add_to_end(1)
A.add_to_end(2)
A.add_to_end(3)
A.add_to_end(4)
A.display()
print()

print("=== add_to_start ===")
A.add_to_start(10)
A.add_to_start(20)
A.display()
print()

print("=== delete head (20) ===")
A.delete(20)
A.display()
print()

print("=== delete middle (2) ===")
A.delete(2)
A.display()
print()

print("=== delete last (4) ===")
A.delete(4)
A.display()
print()

print("=== delete a value not in list (999) ===")
A.delete(999)
A.display()
print()

print("=== delete remaining all ===")
A.delete(10)
A.delete(1)
A.delete(3)
A.display()

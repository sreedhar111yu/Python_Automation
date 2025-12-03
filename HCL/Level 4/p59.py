class Student:
    def __init__(self, student_id, math_mark, science_mark):
        self.student_id = student_id
        self.math_mark = math_mark
        self.science_mark = science_mark
        self.prev = None
        self.next = None


class StudentLinkedList:
    def __init__(self):
        self.head = None

    # INSERT AT END
    def insert_at_end(self, student_id, math_mark, science_mark):
        newNode = Student(student_id, math_mark, science_mark)

        if self.head is None:
            self.head = newNode
            return

        curr = self.head
        while curr.next is not None:
            curr = curr.next

        curr.next = newNode
        newNode.prev = curr

    # INSERT AT START
    def insert_at_start(self, student_id, math_mark, science_mark):
        newNode = Student(student_id, math_mark, science_mark)

        if self.head is None:
            self.head = newNode
            return

        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode

    # INSERT AFTER TARGET
    def after_target(self, target_id, student_id, math_mark, science_mark):
        if self.head is None:
            print("List is empty")
            return

        curr = self.head
        while curr is not None and curr.student_id != target_id:
            curr = curr.next

        if curr is None:
            print("Target not found")
            return

        newNode = Student(student_id, math_mark, science_mark)

        newNode.next = curr.next
        newNode.prev = curr

        if curr.next is not None:
            curr.next.prev = newNode

        curr.next = newNode

    # INSERT BEFORE TARGET
    def before_target(self, target_id, student_id, math_mark, science_mark):
        if self.head is None:
            print("List is empty")
            return

        # If target is head
        if self.head.student_id == target_id:
            self.insert_at_start(student_id, math_mark, science_mark)
            return

        curr = self.head
        while curr is not None and curr.student_id != target_id:
            curr = curr.next

        if curr is None:
            print("Target not found")
            return

        newNode = Student(student_id, math_mark, science_mark)

        prev = curr.prev
        prev.next = newNode
        newNode.prev = prev
        newNode.next = curr
        curr.prev = newNode

    # DELETE NODE
    def delete(self, target_id):
        if self.head is None:
            print("List is empty")
            return

        curr = self.head

        # DELETE HEAD
        if curr.student_id == target_id:
            self.head = curr.next
            if self.head is not None:
                self.head.prev = None
            return

        # FIND TARGET
        while curr is not None and curr.student_id != target_id:
            curr = curr.next

        if curr is None:
            print("Target not found")
            return

        # MIDDLE OR LAST
        if curr.prev is not None:
            curr.prev.next = curr.next

        if curr.next is not None:
            curr.next.prev = curr.prev

    # DISPLAY
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        curr = self.head
        while curr is not None:
            print(f"ID: {curr.student_id} | Math: {curr.math_mark} | Science: {curr.science_mark}")
            curr = curr.next


# ---------------- TEST ----------------

A = StudentLinkedList()
print("INSERT AT END")
A.insert_at_end(1, 89, 90)
A.insert_at_end(2, 69, 70)
A.insert_at_end(3, 99, 90)
A.display()

print("\nINSERT AFTER TARGET (after 2)")
A.after_target(2, 5, 55, 56)
A.display()

print("\nINSERT BEFORE TARGET (before 3)")
A.before_target(3, 7, 88, 77)
A.display()

print("\nDELETE TARGET (delete 2)")
A.delete(2)
A.display()

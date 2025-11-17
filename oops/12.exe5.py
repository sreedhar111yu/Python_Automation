'''Calculating Student Results: Develop a class to accept a student's
 name and marks in three subjects, then calculate and display the total and average marks.'''

class student:
    def __init__(self,name ,roll_no,mark):
        self.name =name
        self.roll_no =roll_no
        self.mark=mark
    
    def total_mark(self):
        stotal_mark=sum(self.mark)
        return stotal_mark
    
    def avg_mark(self):
        avgs_mark=self.total_mark() / int(len(self.mark))
        print(f"average mark is:{avgs_mark}")

s=student('sreedhar',95,[78,75,80,74,77])
print(f"Total mark is :{s.total_mark()}")
s.avg_mark()
        
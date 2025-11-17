'''Build a class Employee with multiple constructors that can 
initialize an employee object in different ways.'''

class Employee:
    def __init__(self,name,id,department):
        self.name=name
        self.id=id
        self.department =department
    
    def dispaly(self):
        print(f"Name of employee:{self.name}, employee id :{self.id}, dep:{self.department}")

E=Employee('Sreedhar V',95,'SDE-1')
E.dispaly()

        
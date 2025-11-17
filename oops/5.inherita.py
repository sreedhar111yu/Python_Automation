class dad:
    def house(self):
        print('red')


class son(dad):
    def company(self):
        print('white')


a=son()
a.company()  #white
a.house() # red



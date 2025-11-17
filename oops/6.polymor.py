'''class dad:
    def house(self):
        print('red')
    
    def house(int a,int b):
        

    def house(srting str):
        
      
s=dad()
s.house(2,3)'''



class BaseView:
    def handle(self):
        return ["base"]

class AuthMixin(BaseView):
    def handle(self):
        return ["auth"] + super().handle()

class CacheMixin(BaseView):
    def handle(self):
        return ["cache"] + super().handle()

class ReportView(AuthMixin, CacheMixin):
    def handle(self):
        return ["report"] + super().handle()

print(ReportView().handle())
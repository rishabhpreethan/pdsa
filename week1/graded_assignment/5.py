class q5:
    def __init__(self,name):
        self.name=name
    
    def sayhi(self):
        print("hello, ",self.name)
        
obj=q5('good morning')
obj.sayhi()
class Student:    
    # Constructor - parameterized    
    def __init__(self, name):    
        print("This is parametrized constructor")    
        self.name = name    
    def show(self):    
        print("Hello",self.name)    
s = Student("Debasish")    
s.show()  

class Emp:  
    def __init__(self,name,id,age):  
        self.name = name;  
        self.id = id;  
        self.age = age  
    def display_details(self):  
        print("Name:%s, ID:%d, age:%d"%(self.name,self.id))  
e = Emp("Debasish",101,32)  
print(e.__doc__)  
print(e.__dict__)  
print(e.__module__)
#print(e.__name__)
#print(e.__bases__)

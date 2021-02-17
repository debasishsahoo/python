class Employee:  
    id = 10;  
    name = "DEBASISH"  
    def display (self):  
        print("ID: %d \nName: %s"%(self.id,self.name))




        
emp = Employee()  
emp.display()

print("Name=",emp.name,"and","Id=",emp.id)

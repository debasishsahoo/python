class Employee:  
    def __init__(self,name,id):  
        self.id = id;  
        self.name = name;  
    def display (self):  
        print("ID: %d \nName: %s"%(self.id,self.name))  
emp1 = Employee("Debasish",101)  
emp2 = Employee("Soubhik",102)
emp3 = Employee("Sourav",103) 
  
#accessing display() method to print employee 1 information  
   
emp1.display();   
  
#accessing display() method to print employee 2 information  
emp2.display();

#accessing display() method to print employee 3 information  
emp3.display(); 

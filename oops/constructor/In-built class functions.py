class Emp:  
    def __init__(self,name,id,age):  
        self.name = name;  
        self.id = id;  
        self.age = age  
  
#creates the object of the class Emp  
e = Emp("Debasish",101,32)  
  
#prints the attribute name of the object s  
print(getattr(e,'name'))  
  
# reset the value of attribute age to 23  
setattr(e,"age",23)  
  
# prints the modified value of age  
print(getattr(e,'age'))  
  
# prints true if the Emp contains the attribute with name id  
  
print(hasattr(e,'id'))  
# deletes the attribute age  
delattr(e,'age')  
  
# this will give an error since the attribute age has been deleted  
print(e.age)  

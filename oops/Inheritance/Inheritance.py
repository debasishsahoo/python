##class Animal:  
##    def speak(self):  
##        print("Animal Speaking")  
###child class Dog inherits the base class Animal  
##class Dog(Animal):  
##    def bark(self):  
##        print("dog barking")  
##d = Dog()  
##d.bark()  
##d.speak()

###############################Multi-Level inheritance######################

##class Animal:  
##    def speak(self):  
##        print("Animal Speaking")  
###The child class Dog inherits the base class Animal  
##class Dog(Animal):  
##    def bark(self):  
##        print("dog barking")  
###The child class Dogchild inherits another child class Dog  
##class DogChild(Dog):  
##    def eat(self):  
##        print("Eating bread...")  
##d = DogChild()  
##d.bark()  
##d.speak()  
##d.eat()


##############################Multiple inheritance######################
##class Calculation1:  
##    def Summation(self,a,b):  
##        return a+b;  
##class Calculation2:  
##    def Multiplication(self,a,b):  
##        return a*b;  
##class Derived(Calculation1,Calculation2):  
##    def Divide(self,a,b):  
##        return a/b;  
##d = Derived()  
##print(d.Summation(10,20))  
##print(d.Multiplication(10,20))  
##print(d.Divide(10,20))

##############################issubclass
##class Calculation1:  
##    def Summation(self,a,b):  
##        return a+b;  
##class Calculation2:  
##    def Multiplication(self,a,b):  
##        return a*b;  
##class Derived(Calculation1,Calculation2):  
##    def Divide(self,a,b):  
##        return a/b;  
##d = Derived()  
##print(issubclass(Derived,Calculation2))  
##print(issubclass(Calculation1,Calculation2))


################################isinstance

##class Calculation1:  
##    def Summation(self,a,b):  
##        return a+b;  
##class Calculation2:  
##    def Multiplication(self,a,b):  
##        return a*b;
##class Calculation3:  
##    def Substraction(self,a,b):  
##        return a*b; 
##class Derived(Calculation1,Calculation2):  
##    def Divide(self,a,b):  
##        return a/b;
##
##d = Derived()  
##print(isinstance(d,Derived))
#############################Method Overriding
##class Animal:  
##    def speak(self):  
##        print("speaking")  
##class Dog(Animal):  
##    def speak(self):  
##        print("Barking")  
##d = Dog()  
##d.speak()

#-------------------------------Real Life Example
##class RBIBank:  
##    def getroilone(self):  
##        return 10;  
##class SBI(RBIBank):  
##    def getroilone(self):  
##        return 7;  
##  
##class ICICI(RBIBank):  
##    def getroilone(self):  
##        return 8;  
##b1 = RBIBank()  
##b2 = SBI()  
##b3 = ICICI()  
##print("Bank Rate of interest:",b1.getroilone());  
##print("SBI Rate of interest:",b2.getroilone());  
##print("ICICI Rate of interest:",b3.getroilone());

######################################Data abstraction
class Employee:  
    __count = 0;  
    def __init__(self):  
        Employee.__count = Employee.__count+1  
    def display(self):  
        print("The number of employees",Employee.__count)  
emp = Employee()  
emp2 = Employee()  
try:  
    print(emp.__count)  
finally:  
    emp.display()  


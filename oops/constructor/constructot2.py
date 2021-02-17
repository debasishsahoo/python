class Student:  
    count = 0  
    def __init__(self):  
        Student.count = Student.count + 1  
s1=Student()  
s2=Student()  
s3=Student()


##i=1  
##n=int(input("Enter the number up to which you want to print the Students numbers?"))  
##for i in range(0,n):  
##    si=Student()

    
print("The number of students:",Student.count)  

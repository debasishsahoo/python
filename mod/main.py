##from calculation import summation    
###it will import only the summation() from calculation.py  
##a = int(input("Enter the first number"))  
##b = int(input("Enter the second number"))  
##print("Sum = ",summation(a,b))
###we do not need to specify the module name while accessing summation()



###the module calculation of previous example is imported in this example as cal.   
##import calculation as cal;  
##a = int(input("Enter a?"));  
##b = int(input("Enter b?"));  
##print("Sum = ",cal.summation(a,b))  



##import json  
##  
##List = dir(json)  
##  
##print(List)  


##from calculation

import calculation   
List = dir(calculation)  
print(List) 

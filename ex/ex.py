##a = int(input("Enter a:"))  
##b = int(input("Enter b:"))  
##c = a/b;  
##print("a/b = %d"%c)  
##  
###other code:  
##print("Hi I am other part of the program")  




##try:  
##    a = int(input("Enter a:"))  
##    b = int(input("Enter b:"))  
##    c = a/b;  
##    print("a/b = %d"%c)  
##except Exception:  
##    print("can't divide by zero")  
##else:  
##    print("Hi I am else block")   

##fileptr = open("file.txt","r")

##try:  
##    #this will throw an exception if the file doesn't exist.   
##    fileptr = open("file.txt","r")  
##except IOError:  
##    print("File not found")  
##else:  
##    print("The file opened successfully")  
##    fileptr.close()

try:  
    fileptr = open("file.txt","r")    
    try:  
        fileptr.write("Hi I am good")  
    finally:  
        fileptr.close()  
        print("file closed")  
except:  
    print("Error")  







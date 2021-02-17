###opens the file file.txt in read mode  
##fileptr = open("file.txt","r")  
##  
##if fileptr:  
##    print("file is opened successfully")
##
##fileptr.close()


print("-----------------------------------------------------------")

###open the file.txt in read mode. causes error if no such file exists.  
##fileptr = open("file.txt","r");   
##  
###stores all the data of the file into the variable content  
##content = fileptr.read(9);   
##  
### prints the type of the data stored in the file  
##print(type(content))   
##  
###prints the content of the file  
##print(content)   
##  
###closes the opened file  
##fileptr.close()

print("-----------------------------------------------------------")


###open the file.txt in read mode. causes error if no such file exists.  
##fileptr = open("file.txt","r");   
##  
###stores all the data of the file into the variable content  
##content = fileptr.readline();   
##  
### prints the type of the data stored in the file  
##print(type(content))   
##  
###prints the content of the file  
##print(content)   
##  
###closes the opened file  
##fileptr.close()

print("--------------------------------------------------------------------------------------------------")

###open the file.txt in read mode. causes an error if no such file exists.  
##  
##  
##fileptr = open("file.txt","r");   
##  
###running a for loop   
##for i in fileptr:  
##    print(i) # i contains each line of the file   

print("-----------------------------------------------------------------------------------------------------")





###open the file.txt in append mode. Creates a new file if no such file exists.  
##fileptr = open("file.txt","a");   
##  
###appending the content to the file  
##fileptr.write("Python is the modern day language. It makes things so simple.")  
##  
##  
###closing the opened file   
##fileptr.close();

print("-----------------------------------------------------------------------------------------------------")


###open the file.txt in read mode. causes error if no such file exists.  
##fileptr = open("file2.txt","x");   
##  
##print(fileptr)  
##  
##if fileptr:  
##    print("File created successfully");

print("-----------------------------------------------------------------------------------------------------")


##with open("file.txt",'r') as f:  
##    content = f.read();  
##    print(content)  

print("-----------------------------------------------------------------------------------------------------")

### open the file file2.txt in read mode  
##fileptr = open("file2.txt","r")  
##  
###initially the filepointer is at 0   
##print("The filepointer is at byte :",fileptr.tell())  
##  
###reading the content of the file  
##content = fileptr.read();  
##  
###after the read operation file pointer modifies. tell() returns the location of the fileptr.   
##  
##print("After reading, the filepointer is at:",fileptr.tell())
print("-----------------------------------------------------------------------------------------------------")

### open the file file2.txt in read mode  
##fileptr = open("file2.txt","r")  
##  
###initially the filepointer is at 0   
##print("The filepointer is at byte :",fileptr.tell())  
##  
###changing the file pointer location to 10.  
##fileptr.seek(10);  
##  
###tell() returns the location of the fileptr.   
##print("After reading, the filepointer is at:",fileptr.tell())
    


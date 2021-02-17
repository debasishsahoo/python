import os;  
  
#creating a new directory with the name new  
##os.mkdir("new")  
##
##
##if mkdir:
##    print("ok")
##else:
##    print("notok")


#changing the current working directory to new   
  
os.chdir("new")

#This method returns the current working directory.
os.getcwd()

#printing the current working directory   
print(os.getcwd())


#removing the new directory   
os.rmdir("new")  

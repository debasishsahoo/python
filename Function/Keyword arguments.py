##
###function func is called with the name and message as the keyword arguments  
##def func(name,message):  
##    print("printing the message with",name,"and ",message)  
##func(name = "John",message="hello") #name and message is copied with the values John and hello respectively  
##
##
### In[3]:
##
##
###The function simple_interest(p, t, r) is called with the keyword arguments the order of arguments doesn't matter in this case  
##def simple_interest(p,t,r):  
##    return (p*t*r)/100  
##print("Simple Interest: ",simple_interest(t=10,r=10,p=1900))
##
##
### In[4]:


#The function simple_interest(p, t, r) is called with the keyword arguments.   
def simple_interest(p,t,r):  return (p*t*r)/100
  
print("Simple Interest: ",simple_interest("t"=10,"r"=10,"p"=1900))

##
### In[1]:
##
##
##def func(name1,message,name2):  
##    print("printing the message with",name1,",",message,",and",name2)  
##func("John",message="hello",name2="David") #the first argument is not the keyword argument
##
##
### In[2]:
##
##
##def func(name1,message,name2):  
##    print("printing the message with",name1,",",message,",and",name2)  
##func("John",message="hello","David")    
##

#!/usr/bin/env python
# coding: utf-8

# In[8]:


x = lambda a:a+10 # a is an argument and a+10 is an expression which got evaluated and returned.   
print("sum = ",x(20))   


# In[9]:


x = lambda a,b:a+b # a and b are the arguments and a+b is the expression which gets evaluated and returned.   
print("sum = ",x(20,10))  


# In[10]:


#the function table(n) prints the table of n  
def table(n):  
    return lambda a:a*n; # a will contain the iteration variable i and a multiple of n is returned at each function call  
n = int(input("Enter the number?"))  
b = table(n) #the entered number is passed into the function table. b will contain a lambda function which is called again and again with the iteration variable i  
for i in range(1,11):  
    print(n,"X",i,"=",b(i)); #the lambda function b is called with the iteration variable i,


# In[11]:


#program to filter out the list which contains odd numbers  
List = {1,2,3,4,10,123,22}  
Oddlist = list(filter(lambda x:(x%3 == 0),List)) # the list contains all the items of the list for which the lambda function evaluates to true  
print(Oddlist) 


# In[12]:


# program to triple each number of the list using map  
List = {1,2,3,4,10,123,22}  
new_list = list(map(lambda x:x*3,List)) # this will return the triple of each item of the list and add it to new_list  
print(new_list)  


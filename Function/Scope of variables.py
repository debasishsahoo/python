#!/usr/bin/env python
# coding: utf-8

# In[1]:


def print_message():  
    message = "hello !! I am going to print a message." # the variable message is local to the function itself  
    print(message)  
print_message()  
print(message) # this will cause an error since a local variable cannot be accessible here.


# In[2]:


def calculate(*args):  
    sum=0  
    for arg in args:  
        sum = sum +arg  
    print("The sum is",sum)  
sum=0  
calculate(10,20,30) #60 will be printed as the sum  
print("Value of sum outside the function:",sum) # 0 will be printed  


#!/usr/bin/env python
# coding: utf-8

# In[1]:


def printme(*names):  
    print("type of passed argument is ",type(names))  
    print("printing the passed arguments...")  
    for name in names:  
        print(name)  
printme("john","David","smith","nick")


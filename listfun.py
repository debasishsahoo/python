# Python program to demonstrate 
# Addition of elements in a List 

# Creating a List 
List = [] 
print("Intial blank List: ") 
print(List) 

# Addition of Elements 
# in the List 
List.append(1) 
List.append(2) 
List.append(4) 
print("\nList after Addition of Three elements: ") 
print(List) 

# Adding elements to the List 
# using Iterator 
for i in range(1, 4): 
	List.append(i) 
print("\nList after Addition of elements from 1-3: ") 
print(List) 

# Adding Tuples to the List 
List.append((5, 6)) 
print("\nList after Addition of a Tuple: ") 
print(List) 

# Addition of List to a List 
List2 = ['For', 'Python'] 
List.append(List2) 
print("\nList after Addition of a List: ") 
print(List) 

# Addition of Element at 
# specific Position 
# (using Insert Method) 
List.insert(3, 12) 
List2.insert(0, 'SIT') 
print("\nList after performing Insert Operation: ") 
print(List) 

# Addition of multiple elements 
# to the List at the end 
# (using Extend Method) 
List.extend([8, 'SCIPY', 'NUMPY']) 
print("\nList after performing Extend Operation: ") 
print(List) 

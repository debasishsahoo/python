# Python program to demonstrate 
# Addition of elements in a Set 

# Creating an empty tuple 
Tuple1 = () 
print("Initial empty Tuple: ") 
print (Tuple1) 

# Creating a Tuple with 
# the use of Strings 
Tuple1 = ('SIT', 'For') 
print("\nTuple with the use of String: ") 
print(Tuple1) 

# Creating a Tuple with 
# the use of list 
list1 = [1, 2, 4, 5, 6] 
print("\nTuple using List: ") 
print(tuple(list1)) 

# Creating a Tuple 
# with the use of loop 
Tuple1 = ('SIT') 
n = 5
print("\nTuple with a loop") 
for i in range(int(n)): 
	Tuple1 = (Tuple1,) 
	print(Tuple1) 

# Creating a Tuple with the 
# use of built-in function 
Tuple1 = tuple('SIT') 
print("\nTuple with the use of function: ") 
print(Tuple1) 

# Creating a Tuple with 
# Mixed Datatypes 
Tuple1 = (5, 'Welcome', 7, 'SIT') 
print("\nTuple with Mixed Datatypes: ") 
print(Tuple1) 

# Creating a Tuple 
# with nested tuples 
Tuple1 = (0, 1, 2, 3) 
Tuple2 = ('python', 'SIT') 
Tuple3 = (Tuple1, Tuple2) 
print("\nTuple with nested tuples: ") 
print(Tuple3) 

# Creating a Tuple 
# with repetition 
Tuple1 = ('SIT',) * 3
print("\nTuple with repetition: ") 
print(Tuple1) 

# Python Program for 
# Formatting of Strings 

# Default order 
String1 = "{} {} {}".format('Python', 'For', 'Life') 
print("Print String in default order: ") 
print(String1) 

# Positional Formatting 
String1 = "{1} {0} {2}".format('Python', 'For', 'Life') 
print("\nPrint String in Positional order: ") 
print(String1) 

# Keyword Formatting 
String1 = "{l} {f} {g}".format(g = 'Python', f = 'For', l = 'Life') 
print("\nPrint String in order of Keywords: ") 
print(String1) 

# Formatting of Integers 
String1 = "{0:b}".format(16) 
print("\nBinary representation of 16 is ") 
print(String1) 

# Formatting of Floats 
String1 = "{0:e}".format(165.6458) 
print("\nExponent representation of 165.6458 is ") 
print(String1) 

# Rounding off Integers 
String1 = "{0:.2f}".format(1/6) 
print("\none-sixth is : ") 
print(String1) 

# String alignment 
String1 = "|{:<10}|{:^10}|{:>10}|".format('SIT','for','Python') 
print("\nLeft, center and right alignment with Formatting: ") 
print(String1) 

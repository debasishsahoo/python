t  = ("hi", "python", 2)  
print (t[1:]);  
print (t[0:1]);  
print (t);  
print (t + t);  
print (t * 3);   
print (type(t))  
##t[2] = "hi";



thistuple = ("apple", "banana", "cherry")
print(thistuple)
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

##thistuple[1] = "blackcurrant"
# The values will remain the same:
print(thistuple)

for x in thistuple:##LOOP
  print(x)

  thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")


  print(len(thistuple))


##del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)


thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

print(x)

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

print(x)





  

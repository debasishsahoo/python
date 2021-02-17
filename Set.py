thisset = {"apple", "banana", "cherry"}
##print(thisset)
####
####for x in thisset:
####  print(x)
####
####print("banana" in thisset)
####
####thisset.add("orange")##To add one item to a set use the add() method.To add more than one item to a set use the update() method.
####
####print(thisset)
####
##thisset.update(["orange", "mango", "grapes","orange", "mango", "grapes"])##Add multiple items to a set, using the update() method
##
##print(thisset)
####
##print(len(thisset))
##
##thisset.remove("banana")##Remove "banana" by using the remove() method
##
##print(thisset)
##thisset.discard("banana")##Remove "banana" by using the discard() method:
##print(thisset)
##thisset = {"apple", "banana", "cherry"}##Remove the last item by using the pop() method:
##
##x = thisset.pop()
##
##print(x)
##
##print(thisset)
##
##
##
##thisset = {"apple", "banana", "cherry"}##The clear() method empties the set:
##
##thisset.clear()
##
##print(thisset)
##
##
##
##thisset = {"apple", "banana", "cherry"}##The del keyword will delete the set completely:
##
##del thisset
##
##print(thisset)
##
##
##thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
##print(thisset)

##
##
##fruits = {"apple", "banana", "cherry"}
##
##x = fruits.copy()
##
##print(x)
##
##
##
##x = {"apple", "banana", "cherry"}
##y = {"google", "microsoft", "apple"}
##
##z = x.difference(y)
##
##print(z)
##x = {"apple", "banana", "cherry"}
##y = {"google", "microsoft", "apple"}
##
##x.difference_update(y) 
##
##print(x)
##
##
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y) 

print(z)
##
##
##x = {"apple", "banana", "cherry"}
##y = {"google", "microsoft", "apple"}
##
##x.intersection_update(y) 
##
##print(x)
##
##
##x = {"apple", "banana", "cherry"}
##y = {"google", "microsoft", "facebook"}
##
##z = x.isdisjoint(y) 
##
##print(z)
##
##
##x = {"a", "b", "c"}
##y = {"f", "e", "d", "c", "b", "a"}
##
##z = x.issubset(y) 
##
##print(z)
##
##
##
##x = {"f", "e", "d", "c", "b", "a"}
##y = {"a", "b", "c"}
##
##z = x.issuperset(y) 
##
##print(z)
##
##
##fruits = {"apple", "banana", "cherry"}
##
##fruits.pop() 
##
##print(fruits)
##
##
##fruits = {"apple", "banana", "cherry"}
##
##fruits.remove("banana") 
##
##print(fruits)
##
##
##x = {"apple", "banana", "cherry"}
##y = {"google", "microsoft", "apple"}
##
##z = x.symmetric_difference(y) 
##
##print(z)
##
##x = {"apple", "banana", "cherry"}
##y = {"google", "microsoft", "apple"}
##
##x.symmetric_difference_update(y) 
##
##print(x)
##
##
##x = {"apple", "banana", "cherry"}
##y = {"google", "microsoft", "apple"}
##
##z = x.union(y) 
##
##print(z)
##
##x = {"apple", "banana", "cherry"}
##y = {"google", "microsoft", "apple"}
##
##x.update(y) 
##
##print(x)
##
##
##

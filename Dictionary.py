##d = {1:'Jimmy', 2:'Alex', 3:'john', 4:'mike'};
##a = {"A":'Jimmy', "B":'Alex', "C":'john', "D":'mike'};
##D = {'Jimmy', 'Alex', 'john', 'mike'};
##print(type(d))
##print(type(D))
##print("1st name is ",d[1]);  
##print("2nd name is "+ d[4]);  
##print (d);
##print (D); 
##print (d.keys());  
##print (d.values());
##print("-------------------------------------------------")
##
##print (D.keys());  
##print (D.values());
##
##
##print("-------------------------------------------------")
##
##print (a.keys());  
##print (a.values());
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##thisdict =	{
##  "brand": "Ford",
##  "model": "Mustang",
##  "year": 1964
##}
##print(thisdict)
####
####
##x = thisdict["model"]
##print(x);
##x = thisdict.get("model")
##
##print(x);
##
##
##thisdict =	{
##  "brand": "Ford",
##  "model": "Mustang",
##  "year": 1964
##}
##thisdict["year"] = "2018"
##print(thisdict["year"])
####
####
##for x in thisdict:
##  print(x +"->"+sting(thisdict.get(x)))
##
##
##
##  thisdict =	{
##  "brand": "Ford",
##  "model": "Mustang",
##  "year": 1964
##}
##del thisdict["model"]
##print(thisdict)
##
##
##
##thisdict =	{
##  "brand": "Ford",
##  "model": "Mustang",
##  "year": 1964
##}
##del thisdict
##print(thisdict) #this will cause an error because "thisdict" no longer exists.
##
##for x in thisdict:
##  print(thisdict[x])

##for x in thisdict.values():
##  print(x)
##
##for x, y in thisdict.items():
##  print(x,y)
##
##
##thisdict =	{
##  "brand": "Ford",
##  "model": "Mustang",
##  "year": 1964
##}
##if "model" in thisdict:
##  print("Yes, 'model' is one of the keys in the thisdict dictionary")
  
##
##
##
##
##
##  print(len(thisdict))
##
##
##


##d = {223:'Jimmy', 120:'Alex', 33333:'john', 4j:'mike'};
##print(d)
##thisdict =	{
##  "brand": "Ford",
##  "model": "Mustang",
##  "year": 1964
##}
##thisdict["color"] = "red"
##print(thisdict)
##
##
##
##thisdict =	{
##  "brand": "Ford",
##  "model": "Mustang",
##  "year": 1964
##}
##thisdict.pop("model")
##print(thisdict)
##
##
##
##thisdict =	{
##  "brand": "Ford",
##  "model": "Mustang",
##  "year": 1964
##}
##thisdict.popitem()
##print(thisdict)
##
##
##
##thisdict =	{
##  "brand": "Ford",
##  "model": "Mustang",
##  "year": 1964
##}
##thisdict.clear()
##print(thisdict)
##
##
##thisdict =	dict(brand="Ford", model="Mustang", year=1964)
### note that keywords are not string literals
### note the use of equals rather than colon for the assignment
##print(thisdict)
##
##
##
##car = {
##  "brand": "Ford",
##  "model": "Mustang",
##  "year": 1964
##}
##
##x = car.copy()
##
##print(x)
##
##
##
##x = ('key1', 'key2', 'key3')
##y = null
##
##thisdict = dict.fromkeys(x, y)
##
##print(thisdict)
##
##
##
##
##x = ('key1', 'key2', 'key3')
##
##thisdict = dict.fromkeys(x)
##
##print(thisdict)
##
##
##car = {
##  "brand": "Ford",
##  "model": "Mustang",
##  "year": 1964
##}
##
##x = car.setdefault("model", "Bronco")
##
##print(x)
##car = {
##  "brand": "Ford",
##  "model": "Mustang",
##  "year": 1964
##}
##
##car.update({"color": "White"})
##
##print(car)
##
##
##car = {
##  "brand": "Ford",
##  "model": "Mustang",
##  "year": 1964
##}
##
##x = car.values()
##
##print(x)
##
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()
print(x)
car["year"] = 2018

print(x)
##
##
##
##

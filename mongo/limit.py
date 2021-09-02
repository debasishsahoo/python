import pymongo

myclient = pymongo.MongoClient("mongodb+srv://root:HQakEtPl45uQeGHM@crudapp.dusom.mongodb.net/pymongo?retryWrites=true&w=majority")
mydb = myclient["pymongo"]
mycol = mydb["customers"]

myresult = mycol.find().limit(5)
#print the result:
for x in myresult:
  print(x)
import pymongo
client = pymongo.MongoClient("mongodb+srv://root:HQakEtPl45uQeGHM@crudapp.dusom.mongodb.net/pymongo?retryWrites=true&w=majority")
db = client["pymongo"]
collection = db["customers"]

#Find First Data
x = collection.find_one()
print(x)

print('----------------------------------------')

#Find All Data
for x in collection.find():
  print(x)

print('----------------------------------------')

#Return Only Some Fields(1)
for x in collection.find({},{ "_id": 0, "address": 1, "name": 1,}):
  print(x)

#Return Only Some Fields(2)
for x in collection.find({},{ "address": 0 }):
  print(x)
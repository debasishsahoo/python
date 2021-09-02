import pymongo
client = pymongo.MongoClient("mongodb+srv://root:HQakEtPl45uQeGHM@crudapp.dusom.mongodb.net/pymongo?retryWrites=true&w=majority")
db = client["pymongo"]
collection = db["customers"]

#Update Single Value
OldValue = { "address": "Valley 345" }
NewValue = { "$set": { "address": "Canyon 123" } }
x =collection.update_one(OldValue, NewValue)

#Update Single Value
OldValue = { "address": { "$regex": "^S" } }
NewValue = { "$set": { "name": "Minnie" } }
y = collection.update_many(OldValue, NewValue)
print(y.modified_count, "documents updated.")

#print "customers" after the update:
for x in collection.find():
  print(x)


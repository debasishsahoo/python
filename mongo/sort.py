import pymongo
client = pymongo.MongoClient("mongodb+srv://root:HQakEtPl45uQeGHM@crudapp.dusom.mongodb.net/pymongo?retryWrites=true&w=majority")
db = client["pymongo"]
collection = db["customers"]

# Sorted Data in Alphabetically order of Name and Asending
AsendingData = collection.find().sort("name")
for x in AsendingData:
  print(x)

# Sorted Data in Alphabetically order of Name and Descending
DescendingData = collection.find().sort("name", -1)
for x in DescendingData:
  print(x)
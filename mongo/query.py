import pymongo
client = pymongo.MongoClient("mongodb+srv://root:HQakEtPl45uQeGHM@crudapp.dusom.mongodb.net/pymongo?retryWrites=true&w=majority")
db = client["pymongo"]
collection = db["customers"]

#Find Single Data With Query
SingleQuery = { "address": "Park Lane 38" }
SingleDoc = collection.find(SingleQuery)
for x in SingleDoc:
  print(x)

#Find Multiple Data With Query
MultipleQuery = { "address": { "$gt": "S" } }
MultipleDocs = collection.find(MultipleQuery)
for x in MultipleDocs:
  print(x)


# Filter With Regular Expressions
RxQuery = { "address": { "$regex": "^S" } }
RxDocs = collection.find(RxQuery)
for x in RxDocs:
  print(x)

# Find Limited Data
LimitDocs = collection.find().limit(5)
#print the result:
for x in LimitDocs:
  print(x)
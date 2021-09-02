import pymongo
client = pymongo.MongoClient("mongodb+srv://root:HQakEtPl45uQeGHM@crudapp.dusom.mongodb.net/pymongo?retryWrites=true&w=majority")
db = client["pymongo"]
collection = db["customers"]

#Delete Single Data
SingleQuery = { "address": "Mountain 21" }
x=collection.delete_one(SingleQuery)
if x:
    print(x.deleted_count, " documents deleted.")
else:
    print('Data Not Delete')

#Delete Multiple Data
MultipleQuery = { "address": {"$regex": "^S"} }
y = collection.delete_many(MultipleQuery)

if y:
    print(y.deleted_count, " documents deleted.")
else:
    print('Data Not Delete')

#Delete All
z = collection.delete_many({})
if z:
    print(z.deleted_count, " documents deleted.")
else:
    print('Data Not Delete')

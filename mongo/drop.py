import pymongo
client = pymongo.MongoClient("mongodb+srv://root:HQakEtPl45uQeGHM@crudapp.dusom.mongodb.net/pymongo?retryWrites=true&w=majority")
db = client["pymongo"]
collection = db["customers"]

x=collection.drop()

if x:
    print("collection deleted.")
else:
    print('collection Not delete')
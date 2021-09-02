import pymongo
client = pymongo.MongoClient("mongodb+srv://root:HQakEtPl45uQeGHM@crudapp.dusom.mongodb.net/pymongo?retryWrites=true&w=majority")
db = client["pymongo"]
collection = db["customers"]

#Insert Single Data
MyData = { "name": "Debasish", "address": "IND" }
x = collection.insert_one(MyData)
print(x.inserted_id)

#Insert Multiple Data 
MyDataList = [
  { "name": "Amy", "address": "UK"},
  { "name": "Hannah", "address": "USA"},
  { "name": "Michael", "address": "SPN"},
  { "name": "Sandy", "address": "AUS"},
  { "name": "Betty", "address": "RSA"},
  { "name": "Richard", "address": "NZ"},
  { "name": "Susan", "address": "WI"},
  { "name": "Vicky", "address": "SCOT"},
  { "name": "Ben", "address": "CHI"},
  { "name": "William", "address": "SING"},
  { "name": "Chuck", "address": "AUS"},
  { "name": "Viola", "address": "USA"}
] 

x = collection.insert_many(MyDataList)
#print list of the _id values of the inserted documents:
print(x.inserted_ids)

#Insert Multiple Data with Custom ID
MyIdList = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]

y = collection.insert_many(MyIdList)
#print list of the _id values of the inserted documents:
print(y.inserted_ids)
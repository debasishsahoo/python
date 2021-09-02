import pymongo
#connection
client = pymongo.MongoClient("mongodb+srv://root:HQakEtPl45uQeGHM@crudapp.dusom.mongodb.net/pymongo?retryWrites=true&w=majority")
db=client['pymongo']
#db = client.test

#Test The Connection
if db:
  print('DB Connected')
else:
  print('DB is Not Connected')



#All DB Name
print(client.list_database_names())

#Check DB Name
dblist = client.list_database_names()
if "pymongo" in dblist:
  print("The database exists.")


#Create Collection
MyCollection = db["customers"]

# All Collection Name
print(db.list_collection_names())

##Check Collection Name
CollectionList = db.list_collection_names()
if "customers" in CollectionList:
  print("The collection exists.")
import pymongo
client = pymongo.MongoClient("mongodb+srv://root:oZHgWotXxCsmwXF3@cluster0.w6udb.mongodb.net/pymongo?retryWrites=true&w=majority")
db=client['pymongo'] #Add your database Name
collection=db['customers'] #Add your collection

#Insert Single Data
Mydata={"name":"Debasish","address":"IND"} #This is RAW Data

x=collection.insert_one(Mydata)

if x:
    print(x.inserted_id)
else:
    print("There is Some issue")







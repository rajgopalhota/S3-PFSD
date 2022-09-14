from pymongo import MongoClient

#create an Instance(Connectivity)
client = MongoClient('mongodb://127.0.0.1:27017')

#create Database
db = client['S3']

#Create Collection
studentdata = db.students

#create Document
student1 = {"regd":"111","Name":"Raja"}
student2 = [{"regd":"222","Name":"Raj"},
            {"regd":"333","Name":"Puja"},
            {"regd":"444","Name":"Pooj"}
]

#Insert Documents
#Insert One Doc
studentdata.insert_one(student1)
# #Insert Many Docs
studentdata.insert_many(student2)



#Retrieve document
#Single Doc
print(studentdata.find_one())
#Multi Doc
for i in studentdata.find():
    print(i)
#Search based on condition
print("\n\nBased on Name search....")
a = {"Name":"Raja"}
for i in studentdata.find(a):
    print(i)

print("\n\nDeleting regd 222................")
#Delete documents
b = {"regd":"222"}
studentdata.delete_one(b)
for i in studentdata.find():
    print(i)


print("\n\nDeleting multiple data................")
c = {"Name":"Raj"}
studentdata.delete_many(c)
for i in studentdata.find():
    print(i)

print("\n\nUpdating 444 with a diff name.................")
#Updating 444 with a diff name
up = {"Name":"Pooj"}
studentdata.update_one(up,{"$set":{"Name":"Kanha"}})
for i in studentdata.find():
    print(i)
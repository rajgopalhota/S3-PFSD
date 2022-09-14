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

#Insert Many Docs
studentdata.insert_many(student2)
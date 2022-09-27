#import pymongo
from pymongo import MongoClient

#creating instance
client = MongoClient("mongodb://127.0.0.1:27017")

#database creation
db = client['Raja']

#collection
subjects = db.Grades

#Creating Docs
s1 = {"Name":"RAJA", "Course":"PFSD", "cgpa":9.3}
s2 = {"Name":"PUJA", "Course":"MSWD", "cgpa":10}


#Inserting Docs
subjects.insert_one(s1)
subjects.insert_one(s2)

#Searching
sub = {"Course":"PFSD"}
for data in subjects.find(sub):
    print(data)

#updating
upd = {"Course":"PFSD"}
d = {"$set":{"Course":"MSWD"}}
subjects.update_one(upd, d)
#
# #deleting
# delt = {"Name":"PUJA"}
# subjects.delete_one(delt)

#printing all

for i in subjects.find():
    print(i)




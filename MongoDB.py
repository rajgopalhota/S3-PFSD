from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['Student']
studentda=db.Student
def add():
   name =input("enter name : ")
   id = input ("enter id : ")
   student={name:id}
   studentda.insert_one(student)
def delete():
    name = input("enter name : ")
    id=input("enter id :")
    tofind1= {name:id}
    for x in tofind1:
        l={name:id}
        print(studentda.find_one(tofind1))
        studentda.delete_one(l)
def modify():
    name = input("enter name : ")
    id = input("enter id :")
    tofind1 = {name: id}
    for x in tofind1:
        l = {name: id}
        print(studentda.find_one(tofind1))
        studentda.delete_one(l)
    name = input("enter name to modify : ")
    id = input("enter id to modify : ")
    student = {name: id}
    studentda.insert_one(student)

o=1
while(o!=0):
    k=input("1.add 2.delete 3.modify 4.exit : ")
    if(k=='1'):
        add()
    if(k=='2'):
        delete()
    if(k=='3'):
        modify()
    if(k=='4'):
        o=0







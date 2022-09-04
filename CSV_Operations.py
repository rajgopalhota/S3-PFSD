import csv
print("Salary Basis...................................")
with open('Employee.csv','rt') as file:
    reader = csv.DictReader(file)
    for row in reader:
        rj = dict(row)
        if int(rj["Salary"]) <= 20000:
            print(rj["Name"],rj["Salary"])
print("Experience Basis...............................")
with open('Employee.csv', 'rt') as file:
    reader = csv.DictReader(file)
    for row in reader:
        rj = dict(row)
        if int(rj["Years Of Experience"]) >= 10:
            print(rj["Name"], rj["Years Of Experience"])
print("Leaves Basis....................................")
with open('Employee.csv', 'rt') as file:
    reader = csv.DictReader(file)
    for row in reader:
        rj = dict(row)
        if int(rj["No of Leaves"]) > 2:
            print(rj["Name"], rj["No of Leaves"])

key1 = input("Enter Employee Id to search")
key2 = input("Enter Employee Name to search")
with open('Employee.csv', 'rt') as file:
    reader = csv.DictReader(file)
    for row in reader:
        rj = dict(row)
        if rj["Name"] == key2 and rj["Emp ID"] == key1:
            print(rj)
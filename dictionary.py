a={}
b=()
c=[]
print(type(a),type(b),type(c))
d1={"RAJA":"Paneer","PUJA":"Tikka masala","RAM":"Roti","Shubham":{"B":"Maggie","L":"Paneer","D":"Roti"}} #1st Is the key and after collon is the value
print(d1)
print(d1["RAJA"]) #find value of the key raja
print(d1["Shubham"])
print(d1["Shubham"]["B"])#keys mustbe immutable
d1["Ankit"]="Burgers"
d1[420]="Kebab"
#this can be even added as follows
d1.update({"Leena":"Toffee"})
print(d1)
del d1[420]
print(d1)
d2=d1.copy()
del d2["Ankit"]
print(d2)
print(d1.keys())
print(d1.items())
class med:
    a="null"
    def  __init__(self,a):
        self.a=a
    def show(self):
        print("no of meds: ",self.a)
class doc(med):
    b="null"
    c ="null"
    def __init__(self,a,b,c):
        super().__init__(a)
        self.b=b
        self.c=c
    def disp(self):
        print("name ",b)

        print("specification ",c)
class pat(doc):
    d="null"
    e="null"
    def __init__(self,a,b,c,d,e):
        super().__init__(a,b,c)
        self.d=d
        self.e=e
    def dipsplay(self):
        print("enter id ",d)
        print("enter name ",e)
e=input("enter name ")
d=input("enter your id ")
c=input("enter doctor name ")
b=input("enter doctor sp ")
a=input("no of meds ")
obj=pat(a,d,c,d,e)
obj.dipsplay()
obj.disp()
obj.show()
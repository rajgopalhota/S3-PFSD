import math
class Abc:
    def perarea(self, a=10,b=20,c=30):
        self.a = a
        self.b = b
        self.c = c
        perimeter = 2 * (a + b)
        area = a * b
        print("perimeter and area of rectangle :")
        print("perimeter is:", perimeter,"\n","Area is:", area, "\n")
        area = 3.17 * a * a
        perimeter = 2 * 3.17 * a
        print("perimeter and area of Circle :")
        print("perimeter is:", perimeter, "\n", "Area is:", area, "\n")
        s = a + b + c
        manu = (s * (s - a) * (s - b) * (s - c))
        area = math.sqrt(manu)
        perimeter = a + b + c
        print("perimeter and area of Triangle :")
        print("perimeter is:", perimeter, "\n", "Area is:", area, "\n")
x = Abc()
x.perarea()
x.perarea(1,2,3)
x.perarea(4,5)
import math


class Abc:
    def rectangle(self, a, b):
        perimeter = 2 * (a + b)
        area = a * b
        print("perimeter and area of rectangle :")
        print("perimeter is:", perimeter,"\n","Area is:", area, "\n")

    def circle(self, a):
        area = 3.17 * a * a
        perimeter = 2 * 3.17 * a
        print("perimeter and area of Circle :")
        print("perimeter is:", perimeter, "\n", "Area is:", area,"\n")

    def triangle(self, a, b, c):
        s = a + b + c
        manu = (s * (s - a) * (s - b) * (s - c))
        area = math.sqrt(manu)
        perimeter = a + b + c
        print("perimeter and area of Triangle :")
        print("perimeter is:", perimeter, "\n", "Area is:", area, "\n")


x = Abc()
x.rectangle(1, 2)
x.circle(1)
x.triangle(1, 2, 3)

# Take  the three  side for the triangle's  from  the  user and check  whether  the  triangle  is equilateral ,isosceles
# or scalene  triangle


from tkinter import Y


x =  int(input("Enter  first side:"))
y =  int(input("Enter second  side:"))
z =  int(input("Enter third:"))


if  x == y == z:
    print("Equilateral Triangle")
elif x==y  or y==z or z==x:
    print("Isosceles Triangle")
else:
    print("Scalene Traingle")
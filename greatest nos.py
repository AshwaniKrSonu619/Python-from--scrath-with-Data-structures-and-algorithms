# write  a program  to take three  input  for  x,y and z .Then compare  and find the largest  value among  the three number 

x = int(input("Enter value of x:"))
y= int(input("Enter value of y:"))
z = int(input("Enter value of z:"))



if x>y and x>1:
    print(x,"is greater value")
elif y>z:
    print(y,"is greater value")
else:
    print(z,"is greater value")
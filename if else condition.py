# Take  an integer  from  user as an input, find  whether  number  is divisible  by 3  or not .
# If divisible then check  whether it is divisible  by 5 or not.


x = int(input("Enter Integer number:"))
if  x%3==0:
    print("Number divisible by 3:")
if x/5==0:
    print("Number divisible by 5:")
else:
    print("Number is not divisible by 5:")
    print()
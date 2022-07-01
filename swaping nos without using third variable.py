# Write  a program to accept 2 number and swap them without using 3rd variable.

a = int(input("Enter First Number:"))
b = int(input("Enter the Second number:"))

a = a+b
b = a-b
a = a-b

print()

print("After Swapping a is:",a)
print("After Swapping b is:",b)
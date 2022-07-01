# Write  the program  to check  the number  is palindrome  or not.


i =int(input("Enter Number:"))
rev = 0
x = i
while(i>0):
    rev = (rev*10)+i%10
    i = i//10
if(x==rev):
    print(x,"is palindrome number:")
else:
    print(x,"is not palindrome number:")
    


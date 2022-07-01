# Write a  program to find the number  is Armstrong   number or not .

from unicodedata import digit

from numpy import digitize


num = int(input("Enter a number:"))
sum = 0

temp = num
while temp>0:
    digit =temp%10
    sum+= digit**3
    temp//=10
if num==sum:
    print(num,"is Armstrong Number")
else:
    print(num,"is not a Armstrong ")


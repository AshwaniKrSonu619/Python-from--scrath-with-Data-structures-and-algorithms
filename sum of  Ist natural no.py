# WAP  to print  the sum of  1st nth natural numbers using while loop


sum = 0
num = int(input("Enter a number:"))
while(num>0):
    sum+=num
    num -=1
  #this will print till infinite loop to stop it we will use break after printing function
print("The result is:",sum)
    
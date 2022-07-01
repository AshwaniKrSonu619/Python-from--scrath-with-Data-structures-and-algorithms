#  WAP to reverse a number 
# input -: 7546
# output-: 6457

i = int(input("input:"))
rev = 0
while(i>0):
    rev = (rev*10)+i%10
    i = i//10
    print("output",rev)

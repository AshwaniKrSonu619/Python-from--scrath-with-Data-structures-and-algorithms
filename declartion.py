# Declare  a student's score  in 5 subjects .Calculate total score and percentage.


sub1 =  int(input("Math:"))
sub2 = int(input("Physics:"))
sub3 = int(input("History:"))
sub4 = int(input("English:"))
sub5 = int(input("Chemistry:"))


print()


total  = sub1+sub2+sub3+sub4+sub5
print("Total Score:",total)
percentage =(total/500)*100
print("Percentage:",percentage,"%")
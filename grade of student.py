# WAP  to display  the grade  
#   Constraints  -:
#   75 & above       -: A grade 
#   60-74            -: B grade 
#   35-59            -: c grade
#   Below  35        -:  Fail



marks =  int(input("Enter Marks:"))

if (marks>=75):
    print("A grade")
elif(marks>=60):
    print("B grade")
elif(marks>=35):
    print("C grade")
elif(marks<=35):
    print("Fail")

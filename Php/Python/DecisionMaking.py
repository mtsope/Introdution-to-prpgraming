
print("********** Simple decision if statements ********")
age = input("How old are you?")
citizen = input("Are you a citizen? Y/N")
if age >= 18 and citizen == 'Y':
   print("You are eligible to vote in the Mozambique")
   print("Congratulations")
else:
    print("You are too young to vote in Mozambique")
    print("To Bad")

print("End of the program")

if age == 65:
 print("You are eligible for social security")



 print("********** Complex decision  if statements ********")
 numGrade = input("Enter the numerical grade")
 if numGrade >= 90:
     letterGrade = "A"

 elif numGrade >= 80:
     letterGrade = "B"

elif numGrade >= 70:
     letterGrade = "C"

elif numGrade >= 60:
     letterGrade = "D"

else:
     letterGrade = "F"

print ("The letter grade is {}".format(letterGrade))
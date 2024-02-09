"""
This Program going to get 03 grades from a student
and checks whether they passed or failed
"""

  grade1 = 12 #Compilation Error - unexpected indent
grade2 = "13" #Compilation Error - number2 variable was assigned with a string value
grade3 = 10

#Runtime Error - trying to add integer values with a string
#Logical Error - Doing the division first and then adding. Need "()" to first add
#and then to the division
result = grade1 + grade2 + grade3 / 3 

print(result)
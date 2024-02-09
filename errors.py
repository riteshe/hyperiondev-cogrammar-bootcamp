# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

#Syntax Error - Missing Parentheses
#Compilation error - incorrect space indentation
print("Welcome to the error program")

#Syntax Error - Missing Parentheses
#Compilation error - incorrect space indentation
print("\n")

# Variables declaring the user's age, casting the str to an int, and printing the result

#Compilation error - incorrect space indentation
#Syntax Error - have to be only one equal sign (=) and 
#need to remove "Years Old"
age_Str = "24" 

#Compilation error - incorrect space indentation
age = int(age_Str) 

#Compilation error - incorrect space indentation
#Runtime error - 'age' needs to be cast to a str()
print("I'm " + str(age) + " years old.")

# Variables declaring additional years and printing the total years of age
#Compilation error - incorrect space indentation
years_from_now = "3"

#Compilation error - incorrect space indentation
#Runtime error - 'years_from_now' needs to be cast to a int()
total_years = age + int(years_from_now)

#Syntax Error - Missing Parentheses
#Logical Error - variable "answer_years" dont exist, should be "total_years"
#Runtime error - 'total_years' needs to be cast to a str()
print("The total number of years: " + str(total_years))

# Variable to calculate the total amount of months from 
#the total amount of years and printing the result

#Logical Error - variable "total" dont exist, should be "total_years"
total_months = total_years * 12

#Syntax Error - Missing Parentheses
#Runtime error - 'total_months' needs to be cast to a str()
#Logical Error - Need to add more 06 months to get the correct number of months
print("In 3 years and 6 months, I'll be " + str(total_months + 6) + " months old")

#HINT, 330 months is the correct answer
"""
Program continually ask the user to enter a number until
the number is different then -1.

when user enter -1, the program calculate the average
of the numbers entered, excluding the -1.
"""

i = 0 #variable to count the input numbers
number = 0 #variable to save the input number
numbers_sum = 0 #variable to sum the inputted numbers

#while loop asking for a number until user enter -1
while number != -1:
    i += 1 #increment by 1 the count of numbers
    numbers_sum += number #sum the inputted number

    #ask user to input a number
    number = int(input("Please enter a number: "))

#decrease by one so the variable dont count the -1 input 
i -= 1

#calculate the average
sum_average = numbers_sum / i

#print the average
print(f"The average is: {sum_average}")
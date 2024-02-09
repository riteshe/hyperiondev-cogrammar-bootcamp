"""
The program ask how many students the user
want to register and the program continue 
only if user input a valid number.
The program open the file if exist otherwise
create new file and write the student ID
in to the file.

"""

#while loop
while True:
    student_quantity = input("How many students are you registering? ")
    if student_quantity.isdigit(): #if the user input is a digit
        with open('reg_form.txt', 'a+') as f: #open/create the file to write
            for i in range(0, int(student_quantity)): #for loop 
                student_id_number = input("Please, enter the student ID number: ")
                f.write(student_id_number+" - ..................\n") #write the student id to the file
            break
"""
The program open a txt file "DOB.txt".
For each line of the file, the program
split the line and put the name on
'names' variable and date on 'dates' varibale.
After closing the file the program print
the names and birthdates.

"""

names = ""
dates = ""
splited_line = ""

with open('DOB.txt', 'r+') as f: # Open the file
        for line in f: #for each line split the line
                splited_line = line.split(" ",2)
                names = names + splited_line[0] + " " +splited_line[1] +"\n"
                dates = dates + splited_line[2]


print("Name")
print(names)#print the names 
print("Birthdate")
print(dates)#print the Birthdates

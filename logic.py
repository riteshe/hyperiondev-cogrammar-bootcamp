#When age is equal to 1,4, 13, 17 or 31 it will print "Old Adult"
#To correct this need to put greater then or equal sign

my_age = 1


if (my_age > 1) and (my_age <= 3):
    print("I'm toddler")
elif (my_age > 4) and (my_age <= 12):
    print("I'm Child")
elif (my_age > 13) and (my_age <= 16):
    print("I'm teenager")
elif (my_age > 17) and (my_age <= 30):
    print("I'm young Adult")
elif (my_age > 31) and (my_age <= 45):
    print("I'm Middle-aged Adult")    
else:
    print("Old Adults")
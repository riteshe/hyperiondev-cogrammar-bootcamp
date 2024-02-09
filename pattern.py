"""
using one "for" and "if and else" statment the program
have to output the following:

*
**
***
****
*****
****
***
**
*

"""

#initialize varibale n
n = 1

#first come the for loop, starting in 1 and ending on 9
for i in range(1,10):
    #inside the for loop, if statement going to check the value of i
    if i <= 5: 
        print("* "*i) # print * multiply by i
    else: # else i is greater then 5
        n += 1 # increment n by 1
        print("* "*(i - n)) # print * multiply by with the result of i - n
        n += 1 # increment again n by 1
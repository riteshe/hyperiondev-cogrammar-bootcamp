"""
Program Start

Ask for the swimming time in minutes
Store the answer on variable swimming_time

Ask for the cycling time in minutes
Store the answer on variable cycling_time

Ask for the running time in minutes
Store the answer on variable running_time

sum all three time and save it on variable triathlon_time

if triathlon_time greater then 0 and less than or equal to 100
print the award

else if triathlon_time greater then 100 and less than or equal to 105
print the award

else if triathlon_time greater then 105 and less than or equal to 110
print the award

else print No Award

Program End
"""

swimming_time = int(input("Please, Enter the time in minutes for swimming: "))
cycling_time = int(input("Please, Enter the time in minutes for cycling: "))
running_time = int(input("Please, Enter the time in minutes for running: "))

#saving all three time on variable triathlon_time
triathlon_time = swimming_time + cycling_time + running_time

if(triathlon_time > 0) and (triathlon_time <= 100):
    print("Award: Provincial Colours")
elif(triathlon_time > 100) and (triathlon_time <= 105):
    print("Award: Provincial Half Colours")
elif(triathlon_time > 105) and (triathlon_time <= 110):
    print("Award: Provincial Scroll")
else:
    print("No Award")
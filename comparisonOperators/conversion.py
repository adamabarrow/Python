'''
The Objective is to make a program that can complete different conversions. The tasks to complete are:
1. Have the user input a number of miles.
2. Convert the number of miles to yards, feet, and inches.
3. Print out the conversions with a simple statement


@author: Adama
'''
#Use input() to get the number of miles from the user. And store
#that int in a variable called miles.

miles = input("Number of miles")

#Convert miles to yards, using the following:
# 1 mile = 1760 yards.
#
#Store the value in a variable called yards and print it out with a 
#simple statement.

yards = int(miles) * 1760
print(str(miles) + " miles in yards is " + str(yards))

#Convert miles to feet, using the following:
# 1 mile = 5280 feet.
#
#Store the value in a variable called feet and print it out with a 
#simple statement.

feet = int(miles) * 5280
print(str(miles) + " miles in feet is " + str(feet))

#Convert miles to inches, using the following:
# 1 mile = 63,360 inches.
#
#Store the value in a variable called inches and print it out with a 
#simple statement.

inches = int(miles) * 63360
print(str(miles) + " miles in inches is " + str(inches))


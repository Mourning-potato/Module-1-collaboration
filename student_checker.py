# Author: Edward B. Bowen Jr.
# Filename: student_checker
# Description: The app asks the student to enter their name, and GPA, and tells them if they have made the honor roll
lName = input("Enter your last name, or ZZZ to exit the program ")
print(lName)
if lName != "ZZZ":
    fName = input("Enter your first name ")
    GPA = float(input("Enter your GPA "))
    if GPA >= 3.5:
        print(fName + " " + lName + " has made the dean's list!")
    if GPA >= 3.25:
        print(fName + " " + lName + " has made the honor roll!")
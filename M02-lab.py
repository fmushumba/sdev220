#Name: Fluer Mushumba
#file name: M02-lab.py
# The app asks for students their names and GPA and tests if they are on honor roll or dean's list
last_name=input("please enter your last name: ")
first_name=input("please enter your first name: ")
gpa=float(input("Please enter your GPA: "))
if gpa>=3.5:
    print("You have made it to the Dean's list")
elif gpa>=3.25:
    print("You have made it to the Honor roll")

while last_name!='ZZZ':
    last_name=input("please enter your last name: ")
    if last_name=='ZZZ':
        break

    first_name=input("please enter your first name: ")
    gpa=float(input("Please enter your GPA: "))
    if gpa>=3.5:
        print("You have made it to the Dean's list")
    elif gpa>=3.25:
        print("You have made it to the Honor roll")


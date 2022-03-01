# question 4 on the lab
# Fabio Fabrizi

# Write the function doAdd(students) - what does this do?
# Read in student's name
# Read in module names and grades
# Test the function, it should create a student dict that we can print out.
# We should add the student dict to list (pass the list in)
# Test this

students= []
def readModules():
    return []
def doAdd(students):
    currentStudent = {}
    currentStudent["name"]=input("enter name :")
    currentStudent["modules"]= readModules()

    students.append(currentStudent)
#test
doAdd(students)

doAdd(students)
print (students)
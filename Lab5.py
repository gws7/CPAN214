# Lab 5

students = {
    1 : {
        "name" : "Gabriel", "age" : 21, "schoolName" : "Humber", "completedCourses" : {
            "Python" : 90, "Java" : 80, "C#" : 90
        },
        "ongoingCourses" : {
            "Stats" : 80, "English" : 90
        }  
    },
    
    2 : {
        "name" : "Alex", "age" : 19, "schoolName" : "Humber", "completedCourses" : {
            "Python" : 70, "Java" : 80,
        },
        "ongoingCourses" : {
            "Stats" : 60, "English" : 70, "C#" : 70
        }  
    },
    
    3 : {
        "name" : "Jaden", "age" : 21, "schoolName" : "Humber", "completedCourses" : {
            "Python" : 90
        },
        "ongoingCourses" : {
            "Stats" : 80, "English" : 90, "C#" : 80, "Java" : 70
        }  
    },
}


def viewAll():
    for student in students:
        printSpecific(student)       


# Using the provided id, run through the dictionary and print the student info    
def printSpecific(id):
    print(f"""
          Student Information:
          ID: {id}, Name: {students[id]["name"]}, Age: {students[id]["age"]}, School: {students[id]["schoolName"]}
          Ongoing Courses: {students[id]["ongoingCourses"]} 
          Completed Courses: {students[id]["completedCourses"]} 
          """)

# Similar to printSpecific, however more focused on ongoing courses
def viewOngoing(id):
    print(f"""
          Student Ongoing Grades:
          {students[id]["ongoingCourses"]}
          """)

# Similar to printSpecific, however more focused on completed courses
def viewCompleted(id):
    print(f"""
          Student Completed Grades:
          {students[id]["completedCourses"]}
          """)

# Getting the values of each completed course in a list format, we take each value and calculate the average
def viewAverage(id):
    iterations = 0
    average = 0
    for value in (list(students[id]["completedCourses"].values())):
        average += value
        iterations += 1
    average = average / iterations
    print(f"Your average so far is: {average:.2f}")
    
# Takes two inputs, the id of student and the course
def viewSpecificOfStudent(id, course):
    print(f"Student Name: {students[id]["name"]}, Course: {course} {(students[id]["completedCourses"]).get(course)}")
    
# Validation function for single input methods, this just checks if ID exists, and if so passes the function with the id
def validation(func):
    idChoice = int(input("Enter Student ID: "))
    if (idChoice not in students):
        print("Wrong Entry, try again")
    else:
        func(idChoice)
        
# Same as single validation, but works for multiple parameters for the 6th option
def validationMultiParam(func):
    idChoice = int(input("Enter Student ID: "))
    courseChoice = input("Enter the course name: ")
    if ((idChoice not in students) and (courseChoice.capitalize() not in students[idChoice]["completedCourses"])):
        print("Wrong Entry, try again")
    else:
        func(idChoice, courseChoice.capitalize())

# TESTING
# print((students[1]["completedCourses"]).get("Java"))
# print(list(students[1]["completedCourses"].values()))
# printSpecific(1)
# viewAll()
# print(students[1]["completedCourses"])

while True:
    choice = int(input("What would you like to do?\n1 - Print all student information\n2 - View specific student information\n3 - View all ONGOING grades of a student\n4 - View all COMPLETED grades of a student\n5 - View average of COMPLETED grades\n6 - View specific grade of X student\n"))
    # Switch statement to work with different cases
    match choice:
        case 1:
            viewAll()
        case 2:
            validation(printSpecific)
        case 3:
            validation(viewOngoing)
        case 4:
            validation(viewCompleted)
        case 5:
            validation(viewAverage)
        case 6:
            validationMultiParam(viewSpecificOfStudent)
        case _:
            print("Invalid Choice")
    again = input("Do you want to continue? (y/n)")
    if (again.lower() == "y"):
        continue
    else:
        break
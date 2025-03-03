# Week 6 was online for a lab
# Classes - Dictionaries - List Comprehension

# Classes are templated, objects are instances/entities that hold various attributes and methods towards it

class Cake: 
    num_eggs = 3
    
cake = Cake()
print(cake.num_eggs)

print("===")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    # Self is the reference to the class instance you are currently calling it to
    def greeting(self):
        print(f"Hi, your name is {self.name} and I am {self.age}")
        
    # Can be renamed however it is always the first thing passed in class functions
    # def greeting(this):
    #     print(f"Hi, your name is {this.name} and I am {this.age}")

person1 = Person("John", 12)
person2 = Person("Jake", 20)
print(person1.age)
print(person2.age)

print("===")

person1.greeting()
person2.greeting()

print("===")

person1.age = 30
print(person1.age)

# This will cause an error as you have deleted the attribute age of the object person1
# del person1.age
# print(person1.age)

print("===")

# pass lets you create empty classes to be filled out later
# You can inherit classes
class Student(Person):
    pass

student1 = Student("Guilherme", 20)
student2 = Student("Gabriel", 20)

student1.greeting()

print("===")

class Student(Person):
    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school

student1 = Student("Jason", 21, "Humber")

student1.greeting()

class Student(Person):
    # Here we override the parent init
    def __init__(self, name, age, school):
        self.school = school

student2 = Student("Tim", 19, "Humber")
# This wont work as you have never initialized a name, age attribute for the Student's constructor.
# student2.greeting()

print("===")

class Student(Person):
    def __init__(self, name, age, school):
        # super() stands for the parent class that the subclass inherits from
        # Way 1: 
        # Person.__init__(self, name, age)
        # Way 2:
        super().__init__(name, age)
        self.school = school
        
    # Method overriding changes the child class method to better suit its needs.
    def greeting(self):
        print(f"Hi, my name is {self.name}, and I am {self.age} years old.\nI study at {self.school}")

student1 = Student("Jason", 21, "Humber")
student1.greeting()
# This allows you to take the parent method
super(Student, student1).greeting()

print("===")

# Dictionaries are used to store values in key value pairs

class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school
        self.grades = {
            "Python" : 90,
            "JavaScript" : 80,
            "C++" : 70 
        }

student1 = Student("James", 20, "York")
print(student1.grades["C++"])

student1.grades["C++"] = 90
print(student1.grades["C++"])

print("===")

# Important Dictionary Facts
# • Duplicate keys not allowed
# • The values in dictionary items can be of any data type
# • Can nest dictionaries inside each other
# • Can get the length of a dictionary using the len function()
# • As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered
# • No dedicated method to index into keys() / values() of the dictionary

# Prints length of key value pairs
print(len(student1.grades))
# Prints type
print(type(student1.grades))
# Prints first key in dict
print(list(student1.grades)[0])
# Prints first value in dict 
print(list(student1.grades.values())[0])

print("===")

# • Trying to access a key that doesn’t exist will return an error
# • get() method that will get value and if doesn’t exist will return None
# • Can get keys in dictionary using key() method
# • Add keys-values by using = operator with unique key

# Get dictionary value using get
print(student1.grades.get("Python"))
# Print all keys
print(student1.grades.keys())
# Trying to get a key that doesnt exist will result in an error
print(student1.grades.get("Boblox")) # Yields None
# print(student1.grades["Boblox"]) # Will give an error

print("===")

# • Update value of key by using the = operator
# • Can also update value by using the update() method
# • Delete keys using the del method
# • Can remove keys using the pop() method
# • Use items() to get all key value pairs as list of tuples

# Prints dictionaries as tuples
print(student1.grades.items())
# Pass key value pair to update
student1.grades.update({"C++" : 100})
# Delete a key from the dict
student1.grades.pop("JavaScript")
print(student1.grades)
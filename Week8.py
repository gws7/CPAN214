# This is after reading week

# Exceptions
# Occurs when something goes wrong, different exceptions are raised for different reasons
# • ImportError: an import fails
# • IndexError: a list is indexed with an out-of-range number
# • NameError: an unknown variable is used
# • SyntaxError: the code can't be parsed properly
# • TypeError: a function is called on a value of an inappropriate type;
# • ValueError: a function is called on a value of the correct type, but with an inappropriate value

# With a Try-Except 
try:
    myList = [1,2,3]
    print(myList[4])
except Exception as err:
    print(err)

# Multiple Exceptions
try: 
    num = 10
    print(num + "Hello")
    print(num/0)
except ZeroDivisionError:
    print("Division By Zero Error")
except(ValueError, TypeError):
    print("Error")

# With a finally clause you can run code no matter what
try:
    myList = [1,2,3]
    print(myList[4])
except Exception as err:
    print(err)
finally:
    print("Finally")
    
# You can use Raise keyword to send a custom error message 
print(1)
# raise ValueError("Custom Error Message")
# print(2)

# Using Raise with Try-Exception block
# try:
#     num = 5/0
# except:    
#     print("Error Occured")
#     raise
# print("Not executed")

# Assertions are used as sanity checks, when an expression is checked if the result comes back false, an exception is raised
# print(1)
# assert 2+2==4
# print(2)
# assert 1+1==3 # Shows an assertion error
# print(3)

# • Often placed at the start of a function to check for valid input, and after a function call to check for valid output
# • The assert can take a second argument that is passed to the AssertionError raised if the assertion fails
# temp = int(input("Enter Temperature: "))
# assert (temp>=0), "COLD"

# Files
# Before editing a file, you must first open it and then edit. There are other options that allow you have more permissions over a file
file = open("C:\Programming\Semester 3\CPAN214 - Python\MyFile.txt")
print(file.read())

try:
    file = open("NewFile.txt", "w")
    file.write("This file has been written")
    file.close()
except Exception as err:
    print(err)
finally:
    file.close()
    
# If you dont run the close operation the file will not run.

# THIS IS THE NEXT SET OF SLIDES
# Used to store multiple items in a single variable, it is not indexed, and is unchangeable, and unordered

numSet = {1,2,3,4,5} # This is a set
wordSet = set(["Spam", "Eggs", "Sausage"]) # This is also a set

emptySet =  set()
print(len(emptySet))
print("eggs" in wordSet)

# What is the main difference?
# Its unorderd, so it cant be indexed, and when its created, it will take its own sorting and also does not take duplicates
randomSet = set([5,1,3,7,3,31,1,5])
print(randomSet) 

randomSet.pop() # Removes a random item
# randomSet.remove(3) # Removes a specific item

print(numSet | wordSet) # | Combines both sets
print(numSet - randomSet) # - Gets items in the first set but not in the second (1st YES, 2nd NO)
print(numSet & randomSet) # & Gets the items in both sets (Common to both sets)
print(numSet ^ randomSet) # ^ Gets the items that are not common to both of them

# Tuples 
# Used to store multiple items in a single variable
# It is ordered, indexed, and unchangeable
numTuple = (1,2,3)
wordTuple = "apple", "banana"

print(numTuple, wordTuple)

# You can access the values in the tuple just as you would with a list but you cannot change stuff
# numTuple[1] = 2 This will give an error

# Tuples are faster than lists and can have multiple data types
emptyTuple = ()
mixedTuple = ("baanana", 1, True)

# Tuple packing without parentheses
packedTuple = "a", 1, "b"
print(packedTuple)
a,b,c = packedTuple
print(a, b, c) # Unpacking puts the variables in order to the specific names

# If a tuple is composed of a list, then the elements inside that list can be changed but not other stuff
tupleWithList = (1,2,3,[1,2])
print(tupleWithList)
tupleWithList[3][1] = 7
print(tupleWithList)

# Can delete a whole tuple using del keyword, and has all same operations as list except anything that changes items

# LIST COMPREHENSION
# An example would be newList = [expression for item in iterable if condition == True]

squaredNumber = [i**2 for i in range(11)]
print(squaredNumber)

evenNumbers = [i for i in range(100) if i % 2 == 0]
# print(evenNumbers)

# None is used like Null, it converts to False when converted to a Boolean variable

a = None
print(a)
print(type(a))

functionVal = print("Assigning something to print yields None")
print(functionVal)
print(type(functionVal))
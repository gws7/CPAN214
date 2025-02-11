def myFunc():
    print("Apple")
    print("Banana")
    print("Orange")
    
# print(myFunc())

def printWithExclamation(word):
    print(f"{word}!")
    
# print(printWithExclamation("hello"))

def printVar(x):
    x += 1
    print(x)
    
# printVar(7)
# print(x) #You will get error because you cannot access x outside of the function scope.

#Parameters refer to the variables in a function definition
#Arguments refer to the value that the parameters take when a function is called.

def max(x,y):
    if x>=y:
        return x
    else:
        return y
    
# print(max(3,5))
# z = max(8,5)
# print(z)

def addNumbers(x,y):
    total = x + y
    return total
    print("This wont run because return ends the function")

# print(addNumbers(5,5))

def multiply(x,y):
    return x*y

a=2
b=4

# operationReassign = multiply
# print(type(operationReassign)) #<class function>
# print(operationReassign(a,b))

def add(x,y):
    return x+y

def doTwice(function, x, y):
    #What happens here is whatever function passed occurs first inside the first function brackets
    #And then with those 2 results the the first functions runs
    return function(function(x,y), function(x,y))

a=2
b=3

# print(doTwice(add, a, b)) # function(2+3=5 , 2+3=5) = 5+5 = 10

#Lambda functions are also known as anonymous functions 
#lambda args : expression
#Can have any number of args but only one expression of which is evaluated and then returned
#The function has no name
#It returns a function object which is assigned to the identifier double
#Can now be called as a normal function

double = lambda x : x*2

# print(double(5))

f = lambda x,y : x+y

# print(f(1,2))

numbers = [1,2,3,4,5,6,7,8,9,10]
#map() takes in a function and an iterator like an array and returns a modified array
#with whatever the function was supposed to do x, an example can be
#map(str.upper, wordsArray)
newNumbers = list(map(lambda x : x*2, numbers))
# print(newNumbers)

numbers = [1,2,3,4,5,6,7,8,9,10]
#filter() this will return a Boolean value based on whether the elements of a list
#after having the applied function are true. So in this case it checks for what numbers 
#are truly even. If true, it will be included in the new list
evenNumbers = list(filter((lambda x : (x%2==0)), numbers))
# print(evenNumbers)
oddNumbers = list(filter((lambda x : not(x%2==0)), numbers))
# print(oddNumbers)

#To use a module just add import moduleName at the top of your code. Its best to import at the top
#Because then everything has access to it.

import random

for i in range(5):
    value = random.randint(1,6)
    print(value)
    
#You can also import specific parts from a module by using the following format 

from math import pi, sqrt
#from random import * can be used to import all objects from the module
print(pi)
print(sqrt(64))

#You can also install modules with the pip in terminal 
#Ex: pip install termcolor
#This will allow you to print in color
#from termcolor import colored
#print(colored("hello","blue"), colored("Yo","green")) #⁡⁣⁢⁢hello⁡ ⁡⁢⁢⁢yo⁡ 


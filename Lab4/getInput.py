import random

def getInputFromUser():
    min = int(input("Enter minimum range value: "))
    max = int(input("Enter maximum range value: "))

    randomNumber = random.randint(min, max)
    
    return randomNumber, min, max


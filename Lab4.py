import random

score = {"wins": 0, "losses": 0}
counter = 1

def getInputFromUser():
    min = int(input("Enter minimum range value: "))
    max = int(input("Enter maximum range value: "))
    return min, max

def randomNumberGenerator():
    randomNumber = random.randint(min, max)
    return randomNumber

def divisionCheck(n):
    if (((n%5)==0) and ((n%3)==0)):
        return "Your guess is divisible by 5 and 3"
    elif ((n%5)==0):
        return "Your guess is divisible by 5"
    elif ((n%3)==0):
        return "Your guess is divisible by 3"

def winPercent(wins, count):
    return round((wins/count),2)

def resetStats():
    global counter
    reset = input("Would you want to reset your score? (y/n)")
    if (reset == "y"):
        score["losses"] = 0
        score["wins"] = 0
        counter = 0

while True:

    #Function returns the values and they are assigned to the variables
    min, max = getInputFromUser()
    randomNumber = randomNumberGenerator()
    
    guess = int(input("Enter your guess: "))
    
    #Passing guess as a parameter, program checks if your number is divisible by 3 or 5, or both
    print(divisionCheck(guess))
    
    if (guess == randomNumber):
        print(f"You have guessed correctly, the number was {guess}")
        score["wins"] += 1
        print(f"Wins: {score['wins']}, Losses: {score['losses']}, total games: {counter}")
        print(winPercent(score["wins"], counter))
    else:
        print(f"Wrong, the number was {randomNumber}")
        score["losses"] +=1
        print(f"Wins: {score['wins']}, Losses: {score['losses']}, total games: {counter}")
        print(winPercent(score["wins"], counter))
    
    #Asks user if they want to reset their game
    resetStats()
       
    cont = input("Would you like to play again? (y/n)")
    if (cont == "y"):
        counter += 1
        continue
    else:
        break
    
    
        


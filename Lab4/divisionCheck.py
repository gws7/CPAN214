def divisionCheck(n):
    if (((n%5)==0) and ((n%3)==0)):
        return "Divisible by 5 and 3"
    elif ((n%5)==0):
        return "Divisible by 5"
    elif ((n%3)==0):
        return "Divisible by 3"
    
# print(divisionCheck(15))
#Lab 6
basketballTeam5 = {"Gabriel", "Steve", "Mario", "Jack", "Ted"}
baseballTeam9 = {"Andrew", "Raph", "John", "Jake", "Chad", "Alex", "Kendrick", "Carti", "Diogo"}
soccerTeam11 = {"Gabriel", "Steve", "John", "Jake", "Chad", "Alex", "Lionel", "Cristiano", "Neymar", "Kylian", "Sergio"}

# ---//---

def fileWriter(file, itemsToAdd):
    with open(file, "w") as file:
        for item in itemsToAdd:
            file.write(item + " ")
    file.close()
            
# fileWriter("C:/Programming/Semester 3/CPAN214 - Python/Lab6/data/basketball_set.txt", basketballTeam5)
# fileWriter("C:/Programming/Semester 3/CPAN214 - Python/Lab6/data/baseball_set.txt", baseballTeam9)
# fileWriter("C:/Programming/Semester 3/CPAN214 - Python/Lab6/data/soccer_set.txt", soccerTeam11)


def fileWriterIntersections(file, set1, set2):
    intersected = set1 & set2
    with open(file, "w") as file:
        for item in intersected:
            file.write(item + " ")
    file.close()
    
# fileWriterIntersections("C:/Programming/Semester 3/CPAN214 - Python/Lab6/data/intersection_basketball_soccer.txt", basketballTeam5, soccerTeam11)
# fileWriterIntersections("C:/Programming/Semester 3/CPAN214 - Python/Lab6/data/intersection_baseball_soccer.txt", baseballTeam9, soccerTeam11)


def fileWriterUnion(file, set1, set2):
    union = set1 | set2
    with open(file, "w") as file:
        for item in union:
            file.write(item + " ")
    file.close()
    
# fileWriterUnion("C:/Programming/Semester 3/CPAN214 - Python/Lab6/data/union_basketball_baseball.txt", basketballTeam5, baseballTeam9)


def fileWriterDifference(file, set1, set2):
    difference = set1 - set2
    with open(file, "w") as file:
        for item in difference:
            file.write(item + " ")
    file.close()
    
# fileWriterUnion("C:/Programming/Semester 3/CPAN214 - Python/Lab6/data/difference_basketball_soccer.txt", basketballTeam5, soccerTeam11)
# fileWriterUnion("C:/Programming/Semester 3/CPAN214 - Python/Lab6/data/difference_baseball_basketball.txt", baseballTeam9, basketballTeam5)

nestedTuple = (1,2,(3,4,(5,6)))

def fileWriterNestedTuple(file, nested):
    with open(file, "w") as file:
        file.write(str(nested))

# fileWriterNestedTuple("C:/Programming/Semester 3/CPAN214 - Python/Lab6/data/nestedtuple.txt", nestedTuple)

def nestedTuples(nested):
    flatTuple = []
    for item in nested:
        if (type(item) == tuple):
            flatTuple.extend(nestedTuples(item))
        else:
            flatTuple.append(item)
    return flatTuple
            
# print(nestedTuples(nestedTuple))
# fileWriterNestedTuple("C:/Programming/Semester 3/CPAN214 - Python/Lab6/data/flattenedTuple.txt")

amount = int(input("Enter the range: "))
evenNumbers = [i for i in range(amount) if i % 2 == 0]
squaredNumbers = [i**2 for i in range(amount)]
print(evenNumbers)
print(squaredNumbers)
#Lab 6
basketballTeam5 = {"Gabriel", "Steve", "Mario", "Jack", "Ted"}
baseballTeam9 = {"Andrew", "Raph", "John", "Jake", "Chad", "Alex", "Kendrick", "Carti", "Diogo"}
soccerTeam11 = {"Gabriel", "Steve", "John", "Jake", "Chad", "Alex", "Lionel", "Cristiano", "Neymar", "Kylian", "Sergio"}

def fileWriter(file, itemsToAdd):
    try:
        with open(file, "w") as f:
            for item in itemsToAdd:
                f.write(f"{item} ")
    except Exception as e:
        print(f"Error writing to {file}: {e}")

def fileWriterIntersections(file, set1, set2):
    try:
        intersected = set1 & set2
        with open(file, "w") as f:
            for item in intersected:
                f.write(item + " ")
    except Exception as e:
        print(f"Error writing to {file}: {e}")

def fileWriterUnion(file, set1, set2):
    try:
        union = set1 | set2
        with open(file, "w") as f:
            for item in union:
                f.write(item + " ")
    except Exception as e:
        print(f"Error writing to {file}: {e}")

def fileWriterDifference(file, set1, set2):
    try:
        difference = set1 - set2
        with open(file, "w") as f:
            for item in difference:
                f.write(item + " ")
    except Exception as e:
        print(f"Error writing to {file}: {e}")

nestedTuple = (1,2,(3,4,(5,6)))

def fileWriterNestedTuple(file, nested):
    try:
        with open(file, "w") as f:
            f.write(str(nested))
    except Exception as e:
        print(f"Error writing to {file}: {e}")

def nestedTuples(nested):
    flatTuple = []
    for item in nested:
        if isinstance(item, tuple):
            flatTuple.extend(nestedTuples(item))
        else:
            flatTuple.append(item)
    return flatTuple

try:
    amount = int(input("Enter the range: "))
    evenNumbers = [i for i in range(amount) if i % 2 == 0]
    squaredNumbers = [i**2 for i in range(amount)]
    
    print(evenNumbers)
    print(squaredNumbers)

    fileWriter("C:/Programming/Semester 3/CPAN214 - Python/Lab6/data/squaredNumbers.txt", squaredNumbers)
    fileWriter("C:/Programming/Semester 3/CPAN214 - Python/Lab6/data/evenNumbers.txt", evenNumbers)
except ValueError:
    print("Please enter a valid integer.")
except Exception as e:
    print(f"Unexpected error: {e}")

fileWriter("C:/Programming/Semester 3/CPAN214 - Python/Lab6/data/basketball_set.txt", basketballTeam5)
fileWriter("C:/Programming/Semester 3/CPAN214 - Python/Lab6/data/baseball_set.txt", baseballTeam9)
fileWriter("C:/Programming/Semester 3/CPAN214 - Python/Lab6/data/soccer_set.txt", soccerTeam11)

fileWriterIntersections("C:/Programming/Semester 3/CPAN214 - Python/Lab6/data/intersection_basketball_soccer.txt", basketballTeam5, soccerTeam11)
fileWriterIntersections("C:/Programming/Semester 3/CPAN214 - Python/Lab6/data/intersection_baseball_soccer.txt", baseballTeam9, soccerTeam11)

fileWriterUnion("C:/Programming/Semester 3/CPAN214 - Python/Lab6/data/union_basketball_baseball.txt", basketballTeam5, baseballTeam9)

fileWriterDifference("C:/Programming/Semester 3/CPAN214 - Python/Lab6/data/difference_basketball_soccer.txt", basketballTeam5, soccerTeam11)
fileWriterDifference("C:/Programming/Semester 3/CPAN214 - Python/Lab6/data/difference_baseball_basketball.txt", baseballTeam9, basketballTeam5)

fileWriterNestedTuple("C:/Programming/Semester 3/CPAN214 - Python/Lab6/data/nestedtuple.txt", nestedTuple)

flattenedTuple = nestedTuples(nestedTuple)
fileWriter("C:/Programming/Semester 3/CPAN214 - Python/Lab6/data/flattenedTuple.txt", flattenedTuple)

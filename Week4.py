fruits = ["apple", "orange", "banana"]
print(fruits[-2])
print(fruits[0])

print("==========")

emptyArray = []
mixedArray = ["Hello", 25, True]
print(mixedArray[1])
print(mixedArray)
print(emptyArray)

print("==========")

nestedArray = [1,2,[3,4,5],6]
print(nestedArray)
print(nestedArray[2])
print(nestedArray[2][1])

print("==========")

text = "Hello"
print(text[1])

print("==========")

nums = [1,1,1,1,1]
nums[2] = 7
print(nums)

print("==========")

nums2 = [1,2,3]
print(nums2 + [4,5,6])
print(nums2 * 3)

print("==========")

fruits = ["apple", "orange", "banana", "pineapple", "kiwi", "grape", "tomato"]
print(fruits[4:])
print(fruits[:3])
print(fruits[1:4])
print(fruits[2:6])

print("==========")

words = ["spam", "egg", "spam", "toast"]
print("spam" in words)
print("egg" in words)
print("toast" in words)
print("tomato" in words)

print("==========")

text = "hello world"
print("world" in text)

print("==========")

print("tomato" not in words) # True because tomato is not in words
print(not "tomato" in words) # True because not negates (tomato in words)
print("world" not in text) #False because world is in text
print("a" not in text) #True because a is not in that string

print("==========")

emptyArray = []
valueArray = [1,2,3]
emptyArray.append(1)
valueArray.append(4)
print(emptyArray)
print(valueArray)

print("==========")

words = ["python", "fun"]
words.insert(1, "is")
print(words)

print("==========")

letters = ["a", "b", "c", "d", "e", "f"]
print(letters.index("c"))
print(letters.index("f"))
# print(letters.index("g")) #Gives error because g is not in array

print("==========")

nums3 = [1,2,3,4,5,6,7,8,9,10,0,1,2,3,4,5]
print(f"Max: {max(nums3)}")
print(f"Min: {min(nums3)}")
print(f"Number of 2s: {nums3.count(2)}") #Can also count occurrences of words

print("==========")

nums3.sort() #You can also sort words with this, putting them in alphabetical order
print(nums3)
nums3.reverse() 
print(nums3)
nums3.remove(8) #This removes the first occurrence, so if there are duplicates, it removes the first one
print(nums3)
nums3.pop(1)
print(nums3)

print("==========")

numberRange = range(10) # Starts at 0 and last number is not inclusive (n-1)
print(numberRange)
print(list(numberRange))

print("==========")

numbers = list(range(8))
print(numbers)
numbers = list(range(3,8)) #Always n-1 at the end, so here last number added is 7
print(numbers)
numbers = list(range(5,20,2)) #1st value is where it starts, 2nd is where it ends, 3rd value is by how much it increases by
print(numbers)
numbers = list(range(20,5,-2))
print(numbers)

print("==========")

fruits = ["apple", "orange", "banana", "pineapple", "kiwi", "grape", "tomato"]
length = len(fruits)
i=0
while (i<length):
    print(f"Fruit: {fruits[i]} = {i}")
    i+=1
    
print("==========")    
    
for fruit in fruits:
    print(f"fruit: {fruit}")

print("==========")   

for char in "Hello World":
    # print(char, end='') #Used to print all the contents in the same line
    print(char)

print("==========")   

for num in range(5):
    print(num)
    
print("==========")   

fruitBox = [["apple", "banana"], ["pineapple", "cherry"], ["melon", "kiwi"]]
for fruitContainer in fruitBox:
    print(f"This is the fruit container's contents: {fruitContainer}")
    for fruit in fruitContainer:
        print(f"These are fruits inside the container: {fruit}")
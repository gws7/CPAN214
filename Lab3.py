nums = []
numEntered = (input("Enter the number(s) (Ex: '1', or '1,2,3,4,5,6') of the list.\n"))

#This is just a simple way to parse the information based on if the user separated the numbers by , or " "
if("," in numEntered):
    nums.extend(numEntered.split(","))
else:
    nums.extend(numEntered.split())    

#This converts each entry from string to number
for i in range(len(nums)):
    nums[i] = int(nums[i])

#This loop is to ask the user if they want to add more numbers
#if Y they will be asked for another number to be enterred and then it is appended
while True:
    addExtra = (input("Want to add another number? (y/n)\n"))
    if addExtra == "n":
        print("No more numbers added")
        break
    else:
        numAdded = int(input("Enter number: "))
        nums.append(numAdded)

#Prints out the max, min, and the nums array
maxNum = max(nums)
minNum = min(nums)
print(f"Nums array finalized: {nums}\nMax={maxNum} and Min={minNum}")    

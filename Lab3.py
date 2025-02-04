nums = []
numEntered = (input("Enter the number(s) (Ex: '1', or '1,2,3,4,5,6') of the list.\n"))
nums.extend(numEntered.split(","))
for i in range(len(nums)):
    nums[i] = int(nums[i])

while True:
    addExtra = (input("Want to add another number? (y/n)\n"))
    if addExtra == "n":
        print("No more numbers added")
        break
    else:
        numAdded = int(input("Enter number: "))
        nums.append(numAdded)

maxNum = max(nums)
minNum = min(nums)
print(f"Nums array finalized: {nums}\nMax={maxNum} and Min={minNum}")    

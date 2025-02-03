my_boolean = True
print(my_boolean)

print("========")

print(2==3)
print("Hello" == "Hello")

print("========")

answer = "Yes"
print ("yes" == answer.lower())

print("========")

print(1 != 1)
print("goodbye" != "hi")
print(7>4)
print(10>=11)

print("========")

#This will be based on the ascii value, the first letter determines the answer and the lower down into the alphabet you go the higher value the letter. Z > A
#Uppercase is always smaller than lower case
print("abc" >= "def")
print("ebc" >= "def")
print("za" >= "az")
print("Toronto" <= "ottawa") # True
print("oronto" <= "ottawa") # True
print("oronto" <= "Ottawa") # False because Uppercase smaller in ASCII than lowercase

print("========")

print(bool(10))
print(bool(""))
print(bool(0))

print("========")

if(10>5):
    print("executed if true")
print("execute regardless")

print("========")

x = 2
y = 1
if(x > y):
    print(f"{x} greater than {y}")
    
print("========")

if(x > y):
    print(f"{x} is greater than {y}")
    if(x == 2):
        print(f"{x} is 2")
        
print("========")

x = 4
y = 20
if(x > y):
    print(f"{x} greater than {y}")
elif(y > x):
    print(f"{y} is greater than {x}")
else:
    print("Else")
    
print("========")

num = 3
if num == 5:
    print("Equals to 5")
elif num == 11:
    print("Equal to 11")
else:
    print("No conditions met")
    
print("========")

#Boolean operators: and, or, not
print(1 == 1 and 2 == 2)
print(3 > 1 or 1>3)
print(2 != 3 and 3 == 3)
print(not 1 == 1)
print(not 1 == 2) #inverts/negates 

print("========")

print(False == False or True)
print(False == (False or True))
print((False == False) or True)

print("========")

i = 0
while(i <= 5):
    print(i)
    i+=1
    
print("========")

#infinite loop
#while 1=1:
#   print("In the loop")

print("========")

#Continue jumps back to the top of the loop (given a certain condition is met)

i = 0 
while(i <= 5):
    i += 1
    if (i == 2 or i == 4):
        print("Skipping 2 and 4")
        continue
    print(i)
    
print("========")

g = 7
while(g != 70):
    print(g)
    g += 7
    
print("========")

x = int(input("Enter a number: "))
print(f"Number entered was {x}")

print("========")

while True:
    #Get numbers as float inputs
    num1 = float(input("Enter number 1: "))
    num2 = float(input("Enter number 2: "))
    
    #Compares which number is bigger
    if(num1>num2):
        print(f"The first number {num1} is greater than the second number {num2}.")
    elif(num2==num1):
        print(f"The two numbers are equal")
        #Continue starts from the top of the loop and does not allow it to exit the program
        continue
    else:
        print(f"The second number {num2} is greater than the first number {num1}")
        
    continue_loop = input("Do you want to continue? (y/n)")
    
    if(continue_loop.lower() == "n"):
        print("Exits Program")
        #Use break to exit a loop/infinite loop
        break
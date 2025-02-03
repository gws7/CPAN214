while True:
    num_elements = int(input("Enter a number: "))
    i = 0
    num_fizz = 0
    num_buzz = 0
    num_fiz_buzz = 0 
    while(i < num_elements):
        i+=1 
        print(f"Iteration {i}")
        if((i % 3) == 0) and ((i % 5) == 0):
            print("FizzBuzz")
            num_fiz_buzz += 1
        elif((i % 5) == 0):
            print("Buzz")
            num_buzz += 1
        elif((i % 3) == 0):
            print("Fizz")
            num_fizz += 1
    print(f"Fizz count: {num_fizz} \nBuzz count: {num_buzz} \nFizzBuzz count: {num_fiz_buzz}")
    
    continue_loop = input("Do you want to continue? (y/n)")
    
    if(continue_loop.lower() == "n"):
        print("Exits Program")
        #Use break to exit a loop/infinite loop
        break
    elif(continue_loop.lower() == "y"):
        continue
    else:
        print("Invalid Input")
        continue_loop = input("Do you want to continue? (y/n)")
        
        
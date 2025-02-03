print(5+3)
print(2-3)
print(5//2)
print(5%2)
print(5/2)
# print(input("Enter your name: "))
print("Gabriel \nSosin")
# print("Hello" + 10) This will not work because you are combining a string with an integer
print("Hello " + str(10)) 
print(int("10") + 10)
print(float("10.5") + 10)
x = 10
print(type(x))
x = "Hello"
print(type(x))
x = None
print(x)
del x
# print(x) this will give an error as you have deleted the variable.
a = 3
a += 3
print(a) 
order = "bread"
order += " and butter"
print(order)
order *=3
print(order)
a, b, c = "Hello ", "There ", "Goobers"
print(a+b+c)
multi = """
Boku a Doctor
Tony Tony Choppa
"""
print(multi)
name = "Gabriel"
print(f"My name is {name}")
print(f"Formatted float addition {(0.1+0.2):0.2f} vs Unformatted {0.1+0.2}")

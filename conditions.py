temperature= 20

if temperature >=30:
    print("Hot Weather")
else:
    print("Normal weather")
    
#if,elif and else
temperature= 40

if temperature >40:
    print("Very Hot Weather")
elif 30<= temperature <=40:
    print("Little Hot")


else: 
    print("Normal weather")

age = 16
if age >= 18:
    print("You are an adult.")
else: 
    print("You are a teenager.")

age = 30
if age >= 18:
    if age <= 25:
        print("You are a young adult.")
    else:
        print("You are an adult.")
else:
    print("You are a child.")

#FizzBuzz Problem

n = int(input("Enter a Number: "))

if n % 3 == 0 and n % 5 == 0:
    print("The number is FizzBuzz")
elif n % 3 == 0:
    print("The number is Fizz.")
elif n % 5 == 0:
    print("The number is Buzz.")
else:
    print("Number is not FizzBuzz")

    
#Checking a number is multiple or not

a = 15
b = 5

if a % b == 0:
    print(f"{a} is a multiple of {b}")
else:
    print(f"{a} is not a multiple of {b}")


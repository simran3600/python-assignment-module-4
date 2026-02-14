# 1. Divisible by 3 using while loop

number = 3

while number <= 1000:
    print(number)
    number = number + 3


# 2. Convert inches to centimeters

inches = float(input("Enter inches (negative number to stop): "))

while inches >= 0:
    centimeters = inches * 2.54
    print("Centimeters =", centimeters)

    inches = float(input("Enter inches (negative number to stop): "))
print("Program ended.")


# 3. Smallest and Largest numbers

numbers = []

while True:
    user_input = input("Enter a number (press Enter to stop): ")
    if user_input == "":
        break

    number = float(user_input)
    numbers.append(number)
print("Smallest number:", min(numbers))
print("Largest number:", max(numbers))


# 4. Guessing game program

import random

number = random.randint(1, 10)

while True:
    guess = int(input("Guess (1-10): "))

    if guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")
    else:
        print("Correct")
        break


# 5. Username and password

attempts = 0

while attempts < 5:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "python" and password == "rules":
        print("Welcome")
        break
    else:
        print("Wrong username or password.")
        attempts = attempts + 1

if attempts == 5:
    print("Access denied")


# 6. Calculate pi using random numbers

import random

N = int(input("How many random points do you want to generate? "))

inside_circle = 0
for i in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x*x + y*y < 1:
        inside_circle += 1

pi = 4 * inside_circle / N
print("Approximate value of pi:", pi)
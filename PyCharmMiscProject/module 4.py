# numbers divisible by three in the range 1 - 1000

num = 1

while num <= 1000:
    if num % 3 == 0:
        print(num)
    num += 1


# convert inches to centimeters

inches = float(input("Enter inches (negative to stop): "))

while inches >= 0:
    cm = inches * 2.54
    print("Centimeters:", cm)

    inches = float(input("Enter inches (negative to stop): "))


# smallest and largest numbers

smallest = None
largest = None

num = input("Enter a number (press Enter to quit): ")

while num != "":
    number = float(num)

    if smallest is None or number < smallest:
        smallest = number

    if largest is None or number > largest:
        largest = number

    num = input("Enter a number (press Enter to quit): ")

print("Smallest number:", smallest)
print("Largest number:", largest)



# random integer between 1 and 10

import random

number = random.randint(1, 10)

guess = int(input("pick a number (1–10): "))

while guess != number:
    if guess > number:
        print("Too high")
    else:
        print("Too low")
    guess = int(input("Guess again: "))

print("Correct!")


# username and password

correct_username = "python"
correct_password = "rules"

attempts = 0

while attempts < 5:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Welcome")
        break
    else:
        print("Wrong username or password")
        attempts += 1

if attempts == 5:
    print("Access denied")



#random points to generate, and calculates the value of pi

import random

n = int(input("How many random points to generate? "))

inside_circle = 0

for i in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x*x + y*y < 1:
        inside_circle += 1

pi = 4 * inside_circle / n

print("Approximate value of pi:", pi)

#while loop to print out all the numbers which are divisible by three in the range of 1-1000

num = 1

while num <= 1000:
    if num % 3 == 0:
        print(num)
    num = num + 1


# convert inches to centimeters

inch = float(input("Enter inches (negative number to stop): "))

while inch >= 0:
    cm = inch * 2.54
    print("Centimeters:", cm)
    inch = float(input("Enter inches (negative number to stop): "))

print("Program ended.")



#smallest and largest number

smallest = None
largest = None
while True:
    num = input("Enter a number (press Enter to quit): ")

    if num == "":
        break

    num = float(num)

    if smallest is None or num < smallest:
        smallest = num

    if largest is None or num > largest:
        largest = num

print("Smallest number:", smallest)
print("Largest number:", largest)



#guess the number

import random

number = random.randint(1, 10)

guess = int(input("pick a number between 1 and 10: "))

while guess != number:
    if guess > number:
        print("Too high")
    else:
        print("Too low")

    guess = int(input("guess again: "))

print("Correct! You guessed the number.")



#username and password

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
        attempts = attempts + 1

if attempts == 5:
    print("Access denied")



#approximate the value of pi using random points

import random

points = int(input("Enter number of points: "))

inside = 0
i = 0

while i < points:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x*x + y*y < 1:
        inside = inside + 1

    i = i + 1

pi = 4 * inside / points
print("Approximate value of pi:", pi)


# sum of the numbers

import random

number  = int(input("Enter number of dice: "))
total = 0

for i in range(number):
    dice = random.randint(1, 6)
    total  = total  + dice
print("sum of the dice  =", total)



# five greatest numbers

numbers = []

while True:
    num = input("Enter a number (press Enter to stop ): ")

    if num == "":
        break

    numbers.append(int(num))
numbers.sort(reverse=True)

print("Five greatest numbers are:")
print(numbers[:5])



# program to check if a number is prime

number  = int(input("Enter a number: "))

prime = True

for i in range(2, number):
    if number  % i == 0:
        prime = False

if number  <= 1:
    prime = False

if prime:
    print(" It is a Prime number")
else:
    print("It is not a prime number")



# name of the cities

cities = []

for i in range(5):
    name = input("Enter city name: ")
    cities.append(name)

for city in cities:
    print(city)




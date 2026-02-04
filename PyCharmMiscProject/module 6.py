# result of each role

import random

def roll_dice():
    return random.randint(1, 6)

result = 0

while result != 6:
    result = roll_dice()
    print(result)


#role playing dice

import random

def roll_dice(side):
    return random.randint(1, side)

sides = int(input("Enter the  number of sides on the dice: "))

result = 0

while result != sides:
    result = roll_dice(sides)
    print(result)


# gallons to liter conversion program

def gallons_to_liters(gallon):
    return gallon * 3.78541

gallons = float(input("Enter  the volume in gallons (negative value to stop): "))

while gallons >= 0:
    liters = gallons_to_liters(gallons)
    print("Volume in liters:", liters)

    gallons = float(input("Enter  the volume in gallons (negative value to stop): "))



#list of integers as a parameter

def sum_of_list(numbers):
    return sum(numbers)

my_list = [1, 2, 3, 4, 5]

result = sum_of_list(my_list)
print(result)


# remove uneven numbers

def remove_odd(numbers):
    even_list = []

    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)

    return even_list

my_list = [1, 2, 3, 4, 5, 6, 7, 8]

new_list = remove_odd(my_list)

print("Original list:", my_list)
print("List without odd numbers:", new_list)


# diameter and price of two pizzas

import math

def pizza_value(diameter, price):
    radius = diameter / 2
    area = math.pi * radius * radius
    area_m2 = area / 10000
    return price / area_m2

d1 = float(input("Enter the diameter of first pizza (cm): "))
p1 = float(input("Enter the price of first pizza (euros): "))

d2 = float(input("Enter the diameter of second pizza (cm): "))
p2 = float(input("Enter the price of second pizza (euros): "))

value1 = pizza_value(d1, p1)
value2 = pizza_value(d2, p2)

if value1 < value2:
    print("First pizza is cheaper per square meter.")
else:
    print("Second pizza is cheaper per square meter.")



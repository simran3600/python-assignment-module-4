# 1. Determine season based on month number

seasons = ("winter", "spring", "summer", "autumn")

month = int(input("Enter month number (1-12): "))

if 1 <= month <= 12:
    season = seasons[(month % 12) // 3]
    print("Season:", season)
else:
    print("Invalid month number")


# 2. New and existing name checker

names = set()

while True:
    name = input("Enter name( press enter to stop): ")

    if name == "":
        break
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)
print("Names entered:")
for name in names:
    print(name)


# 3. Airport data finder

airports = {}
while True:
    choice = input("Enter (1 / 2 / 3 ): ")

    if choice == "1":
        code = input("Enter ICAO code: ")
        name = input("Enter airport name: ")
        airports[code] = name
        print("Airport added.")

    elif choice == "2":
        code = input("Enter ICAO code: ")
        if code in airports:
            print("Airport name:", airports[code])
        else:
            print("Airport not found.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
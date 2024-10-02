# 10/2/2024
# P2LAB2
# Creating a dictionary and allowing the user to pick from it to gather information


# Creating a dictionary using key:value pairs
cars = {"Camaro":18.21, "Prius":52.36, "Model S":110, "Silverado":26, "Mustang":26}

print(cars.keys(), "\n")

# User Selects the vehicle they want to see the mpg for and printing it out
userChoice = input(f"Select a vehicle to see its mpg: ")
print()

print(f"The", userChoice, "gets", cars[userChoice], "mpg")
print()

# Gathering how many miles the user wants to drive

miles = int(input(f"How many miles will you drive the {userChoice}? "))

# Calulating the amount of gas needed

print()
print(f"{miles/cars[userChoice]:.2f} gallon(s) of gas are needed to drive the {userChoice} {miles} miles.")

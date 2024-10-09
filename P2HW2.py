
# 10/9/2024
# P2HW2
# User enters values into a list and we will do math with those values


# User puts their grades into a variable

Module1 = float(input("Enter grade for Module 1: "))
Module2 = float(input("Enter grade for Module 2: "))
Module3 = float(input("Enter grade for Module 3: "))
Module4 = float(input("Enter grade for Module 4: "))
Module5 = float(input("Enter grade for Module 5: "))
Module6 = float(input("Enter grade for Module 6: "))

print()

print("----------Results----------")

# Creates a list
GradesForModules = []

# Add variables to the list
GradesForModules.append(Module1)
GradesForModules.append(Module2)
GradesForModules.append(Module3)
GradesForModules.append(Module4)
GradesForModules.append(Module5)
GradesForModules.append(Module6)

# Displays Lowest Grade
print(f"{'Lowest Grade:':<20}{min(GradesForModules)}")

# Displays Highest Grade
print(f"{'Highest Grade:':<20}{max(GradesForModules)}")

# Displays Sum of Grades
print(f"{'Sum of Grades:':<20}{sum(GradesForModules)}")

# Displays the average
Average = sum(GradesForModules)/len(GradesForModules)
print(f"{'Average:':<20}{Average:.2f}")

# Formatting 
print("-" * 27)

import os
os.system("cls")  # Clear the console

# Logical Operators in Python
# Logical operators are used to combine conditional statements.
print("\n=== Logical operator ===\n")
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False
print("\n")


# or operator
print("\n === or operator === \n")
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False
print("\n")

# not operator
print("\n === not operator === \n")
print(not True)  # False
print(not False)  # True

# and operator with integer values
print("\n === and operator with integer values === \n")
age = 20
licensed = True

if age >= 18 and licensed:
    print("You can drive")
print("\n")

# or operator with string values
print("\n === or operator with string values === \n")
is_student = False
membership = True

if is_student or membership:
    print("You get a discount")
print("\n")

# not operator with string values
print("\n === not operator with string values === \n")
is_admin = False

if not is_admin:
    print("Access denied")

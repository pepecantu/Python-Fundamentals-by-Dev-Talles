import os
os.system("cls")  # Clear the console

# in membership operator
# not in
# membership operators are used to check if a value is present in a sequence (string, list, tuple, set, dictionary)

print("\n Membership Operator in a numbers range \n")

print(9 in range(1, 10))  # True # 9 is in the range of 1 to 10
print(11 in range(1, 10))  # False # 11 is not in the range of 1 to 10
print("a" in "apple")  # True # "a" is in the string "apple"
print("b" in "apple")  # False # "b" is not in the string "apple"
print("a" not in "apple")  # False # "a" is in the string "apple"
print("b" not in "apple")  # True # "b" is not in the string "apple"
print("\n")

print("\n Membership Operators in a fruit list \n")

fruits = ["apple", "banana", "cherry"]  # List of fruits

print("apple" in fruits)  # True # "apple" is in the list of fruits
print("orange" in fruits)  # False # "orange" is not in the list of fruits
print("apple" not in fruits)  # False # "apple" is in the list of fruits
print("orange" not in fruits)  # True # "orange" is not in the list of fruits
print("\n")

sentence = " Iam learning Python programming language"
print("\n Membership Operators in a sentence \n")
print("Python" in sentence)  # True # "Python" is in the sentence
print("Python" not in sentence)  # False # "Python" is in the sentence
print("javaScript" in sentence)  # False # "javaScript" is not in the sentence
print("\n")

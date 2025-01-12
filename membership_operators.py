#Membership Operators
"""
Membership operators are used to check if a value or an item exists in a sequence, such as a string, list, tuple, set, or dictionary.
"""
#Using in
# With strings
print("a" in "apple")  # True, 'a' exists in "apple"
print("z" in "apple")  # False, 'z' does not exist in "apple"

# With lists
numbers = [1, 2, 3, 4, 5]
print(3 in numbers)  # True, 3 exists in the list
print(10 in numbers) # False, 10 does not exist in the list

# With dictionaries (checks keys)
person = {"name": "Alice", "age": 25}
print("name" in person)     # True, 'name' is a key in the dictionary
print("gender" in person)   # False, 'gender' is not a key in the dictionary

#using not in
# With strings
print("z" not in "apple")  # True, 'z' does not exist in "apple"
print("a" not in "apple")  # False, 'a' exists in "apple"

# With lists
fruits = ["apple", "banana", "cherry"]
print("orange" not in fruits)  # True, "orange" does not exist in the list
print("banana" not in fruits) # False, "banana" exists in the list

# With sets
colors = {"red", "green", "blue"}
print("yellow" not in colors)  # True, "yellow" is not in the set
print("red" not in colors)     # False, "red" is in the set

#Case Sensitivity: Membership checks are case-sensitive.
print("a" in "Apple") 
print("a" in "apple") 

#Check if a character is a vowel
char="a"

if char in "aeiou":
    print(f"{char} is Vowel")
else:
    print("Consonant")
    
#Verify if an element exists in a list

shopping_list = ["milk", "bread", "eggs"]
item = "butter"
if item in shopping_list:
    print(f"{item} is already in the list.")
else:
    print(f"{item} is not in the list.")

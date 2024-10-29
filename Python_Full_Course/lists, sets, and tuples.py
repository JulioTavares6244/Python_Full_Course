# collection = single "variable" used to store multiple values
#   List  = [] ordered and changeable. Duplicates OK
#   Set   = {} unordered and immutable, but Add/Remove OK. No duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

# fruits = ["apple", "orange", "banana", "coconut"]
# fruits = {"apple", "orange", "banana", "coconut"}
fruits = ("apple", "orange", "banana", "coconut", "coconut")

# General methods
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)

# List methods
# fruits[0] = "pineapple"
# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.insert(0, "pineapple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("pineapple"))
# print(fruits.count("pineapple"))

# Set methods
# fruits.add("pineapple")
# fruits.remove("apple")
# fruits.pop()
# fruits.clear()

# Tuple methods
# print(fruits.index("apple"))
print(fruits.count("coconut"))

# print(fruits)
# print(fruits[0])
for fruit in fruits:
    print(fruit)
# Iterables = An object/collection that can return its elements one at the time,
#             allowing it to be iterated over in a loop

# lists and tuples
# numbers = (1, 2, 3, 4, 5)

# for number in numbers:
    # print(number)


# sets
# fruits = {"apple", "orange", "banana", "coconut"}

# for fruit in fruits:
    # print(fruit)

# strings
# name = "Julio Tavares"

# for character in name:
    # print(character, end=" ")

# dictionaries
my_dictionary = {"A": 1, "B": 2, "C": 3}


# if you iterate a dictionary, it will returns the keys, but not the values

# for key in my_dictionary.values():
    # print(key)
          
# only using the built-in method ".values" you can do that

# for value in my_dictionary.values():
    # print(value)

# to get both, you need to use the method ".items"

for key, value in my_dictionary.items():
    print(f"{key} = {value}")
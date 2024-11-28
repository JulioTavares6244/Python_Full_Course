# Membership operators = used to test whether a value or variable is found in a sequence
#                        (string, list, tuple, set, or dictionary)
#                        1. in
#                        2. not in

# Strings
# word = "APPLE"

# letter = input("Guess a letter in the secret word: ")

# if letter not in word:
    # print(f"{letter} was not found")
# else:
    # print(f"There is a {letter}")

email = "JulioTavares@gmail.com"

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")

# lists, sets and tuples behave similarly
# students = {"Spongebob", "Patrick", "Sandy"}

# student = input("Enter the name of a student: ")

# if student not in students:
    # print(f"{student} was not found")
# else:
    # print(f"{student} is a student")

# Dictionaries
# grades = {"Sandy": "A", 
#           "Squidward": "B", 
#           "Spongebob": "C", 
#           "Patrick": "D"}

# student = input("Enter the name of a student: ")

# if student in grades:
    # print(f"{student}'s grades is {grades[student]}")
# else:
    # print(f"{student} was not found")
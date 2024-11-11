# keyword arguments = an argument preceded by an identifier
#                     helps with readability
#                     order of arguments doesn't matter 
#                     1. positional, 2. default, 3. KEYWORD, 4. arbitrary

# def hello(greetings, title, first, last):
    # print(f"{greetings} {title}{first} {last}")

# hello("Olá", title="Dr.", last="Hernandes", first="Luiz")

# for x in range(1, 11):
    # print(x, end=" ") # The "end=" in a print (who is built in function) is a keyword argument

# print("1", "2", "3", "4", "5", sep="-") # "sep=" is too a keyword argument

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_number = get_phone(country=55, area=11, first=3599, last=1790)

print(phone_number)
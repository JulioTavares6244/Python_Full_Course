# Calculator Program

num1 = float(input("Type a number: "))
operator = input("Type your operator: ")
num2 = float(input("Type a number: "))

result = print(round(num1 + num2, 2)) if operator == "+" else "This operator is not valid"
result = print(round(num1 - num2, 2)) if operator == "-" else "This operator is not valid"
result = print(round(num1 * num2, 2)) if operator == "*" else "This operator is not valid"
result = print(round(num1 / num2, 2)) if operator == "/" else "This operator is not valid"

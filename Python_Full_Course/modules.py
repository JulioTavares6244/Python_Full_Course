# module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program reusable separate files

# import math
# import math as m
# from math import pi
import example

result = example.pi
result = example.square(9)
result = example.cube(3)
result = example.circumference(3)
result = example.area(9)

print(result)
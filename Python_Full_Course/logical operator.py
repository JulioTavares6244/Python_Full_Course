# logical operator = evaluate multiple conditions (or, and, not)
#                    or  = at least one condition must be True
#                    and = both conditions must be True
#                    not = inverts the condition (not False, not True)

temp = 20
is_sunny = False

if temp >= 28 and is_sunny:
    print("It's HOT outside!")
    print("It's SUNNY!")
elif temp <= 0 and is_sunny:
    print("It's COLD outside!")
    print("It's SUNNY!")
elif 28 > temp > 0 and is_sunny:
    print("It's WARM outside!")
    print("It's SUNNY!")
elif temp >= 28 and not is_sunny:
    print("It's HOT outside!")
    print("It's CLOUDY!")
elif temp <= 0 and not is_sunny:
    print("It's COLD outside!")
    print("It's CLOUDY!")
elif 28 > temp > 0 and not is_sunny:
    print("It's WARM outside!")
    print("It's CLOUDY!")

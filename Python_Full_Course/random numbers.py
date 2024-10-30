# Random library

import random

low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

# d6 = random.randint(1, 6)
# d20 = random.randint(1, 20)
# d100 = random.randint(low, high)
# number = random.random()
# option = random.choice(options)
random.shuffle(cards)

print(cards)
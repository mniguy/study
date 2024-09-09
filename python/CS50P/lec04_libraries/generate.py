# 01
# random.choice(seq=anything like lists)
import random

random.choice(["heads", "tails"])

# 02
from random import choice

coin = choice(["heads", "tails"])
print(coin)

# 03
import random
number = random.randint(1, 10)

# 04
import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)

# 05
import statistics

print(statistics.mean([100, 90]))
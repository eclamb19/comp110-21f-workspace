"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730313907"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint

fortune = randint(1, 4)

fortune_1: str = "You will travel near and far."
fortune_2: str = "You will soon meet a new friend."
fortune_3: str = "Your love life will soon heat up!"
fortune_4: str = "You will inherit a great fortune."

print("Your fortune cookie says...")

if fortune == 1:
    print(fortune_1)
else:
    if fortune == 2:
        print(fortune_2)
    else:
        if fortune == 3:
            print(fortune_3)
        else:
            if fortune == 4:
                print(fortune_4)

print("Now, go spread positive vibes!")
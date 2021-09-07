"""Repeating a beat in a loop."""

__author__ = "730313907"

user_beat: str = input("What beat do you want to repeat? ")
repetition: int = int(input("How many times do you want to repeat it? "))
i: int = 0 
one_line: str = user_beat 

if repetition > 0: 
    while i < repetition:
        one_line = one_line + " " + user_beat
        i = i + 1
    print(one_line)
else:
    print("No beat...")
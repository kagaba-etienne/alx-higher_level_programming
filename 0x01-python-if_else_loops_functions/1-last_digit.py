#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last_digit = (number % 10)
else:
    last_digit = 10 - (number % 10)
decision = ""
if last_digit == 0:
    decision = "is 0"
elif last_digit > 5:
    decision = "is greater than 5"
else:
    decision = "is less than 6 and not 0"
print(f"Last digit of {number} is {last_digit} and {decision}")

#!/usr/bin/python3
import random

# Assign a random signed number to the variable number
number = random.randint(-100, 100)

# Print the assigned number
print(f'The number {number}', end=' ')

# Check if the number is positive, zero, or negative
if number > 0:
    print('is positive')
elif number == 0:
    print('is zero')
else:
    print('is negative')


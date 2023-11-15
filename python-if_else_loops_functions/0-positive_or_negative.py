#!/usr/bin/python3
import random
from tqdm.notebook import tqdm

# Simulate the program execution multiple times to demonstrate its functionality
for _ in tqdm(range(5), desc='Simulating program execution'):
    number = random.randint(-100, 100)
    if number > 0:
        print(f'{number} is positive\n')
    elif number == 0:
        print(f'{number} is zero\n')
    else:
        print(f'{number} is negative\n')

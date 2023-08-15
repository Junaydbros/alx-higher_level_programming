#!/usr/bin/python3
import random
number = random.randit(-1000, 1000)
print(f"Last digit of {number} is {number % 10} ")
if (number % 10) > 5:
    print('and is greater than 5')
elif (number % 10) == 0:
    print('and is 0')
elif (number % 10) < 6 && (number % 10) != 0:
    print('and is less than 6 and not 0')

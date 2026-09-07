from math import gcd
from functools import reduce

# Function to calculate the least common multiple (LCM) of two numbers
def lcm(x, y):
    return x * y // gcd(x, y)

# Function to calculate the LCM of a list of numbers
def lcm_multiple(numbers):
    return reduce(lcm, numbers)

# List of numbers from 1 to 20
numbers = list(range(1, 21))

# Calculate the LCM of the range
result = lcm_multiple(numbers)

# Print the result
print("The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is:", result)

# Function to check if a number is a palindrome
def is_palindrome(number):
    return str(number) == str(number)[::-1]

# Initialize variables to store the largest palindrome and its factors
largest_palindrome = 0
factors = (0, 0)

# Iterate over all pairs of 3-digit numbers
for i in range(999, 99, -1):
    for j in range(i, 99, -1):  # Start from i to avoid duplicate checks and improve efficiency
        product = i * j
        if is_palindrome(product) and product > largest_palindrome:
            largest_palindrome = product
            factors = (i, j)

# Print the result
print("The largest palindrome made from the product of two 3-digit numbers is:", largest_palindrome)
print("Factors:", factors[0], "and", factors[1])

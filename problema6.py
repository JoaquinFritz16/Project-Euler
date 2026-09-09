# Calculate the sum of squares of the first n natural numbers
def sum_of_squares(n):
    return n * (n + 1) * (2 * n + 1) // 6

# Calculate the square of the sum of the first n natural numbers
def square_of_sum(n):
    return (n * (n + 1) // 2) ** 2

# Number of natural numbers to consider
n = 100

# Calculate S1 and S2
S1 = sum_of_squares(n)
S2 = square_of_sum(n)

# Calculate the difference
difference = S2 - S1

# Print the result
print(f"The difference between the sum of the squares of the first {n} natural numbers and the square of the sum is: {difference}")

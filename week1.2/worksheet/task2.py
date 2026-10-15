# Worksheet 1.2: Task 2 Solution
import sys
import util

numbers = util.read_numbers()

if len(numbers) == 0:
    sys.exit("Error: no numbers provided")

numbers.sort()

minimum = min(numbers)
maximum = max(numbers)
mean = sum(numbers) / len(numbers)

n = len(numbers)

if n % 2 == 1:
        median = numbers[n // 2]
else: 
        median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2

print(f"Minimum = {minimum}")
print(f"Maximum = {maximum}")
print(f"Mean = {mean}")
print(f"Median = {median}")
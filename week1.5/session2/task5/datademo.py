# Week 1.5, Session 2: Task 5

# Write a program here to create a Dataset containing data
# from a file named by the user

# Your program should display dataset size, mean and median,
# followed by the individual values (using a for loop)
from data import Dataset

filename = input("Enter filename: ")

dataset = Dataset(filename)

print("Size:", len(dataset))
print("Mean:", dataset.mean())
print("Median:", dataset.median())

print("\nValues:")

for value in dataset:
    print(value)
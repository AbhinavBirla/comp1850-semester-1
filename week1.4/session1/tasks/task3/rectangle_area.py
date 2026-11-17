
# function implementation

def rectangle_area(length, width):  # define suitable input data
    area = length * width
    return area

# testing the function
print(f"Area is {rectangle_area(5, 3)}")

def even_numbers(max_value):
    numbers = []

    for i in range(max_value + 1):
        if i % 2 == 0:
            numbers.append(i)

    return numbers

  
                 # return an appropriate value

# testing the function
print(even_numbers(10))


def mean_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

print(mean_average([2, 4, 6, 8, 10]))

   # provide suitable data matching your inputs

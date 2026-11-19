# Week 1.5, Session 1: Task 4

# Add one or more import statements here to give this program
# access to the Point and Circle classes defined in geometry.py

# Write a program here that
#  - Creates a Point object, to represent the centre of a circle
#  - Creates a Circle object, using the Point object and a value for radius
#  - Displays the area of the circle
#  - Displays the perimeter of the circle
from geometry import Point, Circle

x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))

centre = Point(x, y)

radius = float(input("Enter circle radius: "))

circle = Circle(radius, centre)

print(f"Area: {circle.area():.4f}")
print(f"Perimeter: {circle.perimeter():.4f}")
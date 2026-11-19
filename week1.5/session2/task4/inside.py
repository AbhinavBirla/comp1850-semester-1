# Week 1.5, Session 2: Task 4

# Add a program here that demonstrates use of the __contains__()
# method that you implemented in the Circle class
from geometry import Point, Circle

circle = Circle(5, Point(0, 0))

point = Point(2, 3)

if point in circle:
    print("Point is inside the circle")
else:
    print("Point is outside the circle")
# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

# Copy Point class definition here
class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # Add distance() method here
    def distance(self):
        return math.hypot(self.x, self.y)
    
    # Add distance_to() method here
    def distance_to(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)
    
    # (This will need a parameter representing another point)

# Add a definition for a Circle class here, giving it
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle
class Circle:

    def __init__(self, radius, centre=Point(0.0, 0.0)):
        self.radius = radius
        self.centre = centre

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius 

# Don't add any testing code to this file!

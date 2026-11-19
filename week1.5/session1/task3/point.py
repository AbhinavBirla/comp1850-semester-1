# Week 1.5, Session 1: Task 3
import math
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
p1 = Point(3, 4)
p2 = Point(6, 8)



# Finally, add code here to demonstrate use of Point#
print("p1 coordinates:", p1.x, p1.y)
print("p2 coordinates:", p2.x, p2.y)

print("Distance of p1 from origin:", p1.distance())
print("Distance of p2 from origin:", p2.distance())

print("Distance between p1 and p2:", p1.distance_to(p2))
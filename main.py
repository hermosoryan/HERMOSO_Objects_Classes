print("Name: Ryan Hermoso ")
print("Section: BS COMPUTER SCIENCE 1E ")
print("Instructor: Mr. Ralph Angelo  Baguio ")
print("Date: January  13, 2024")

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        circle_area = math.pi * (self.radius ** 2)
        print(f"Area of the circle with radius {self.radius}: {circle_area:.2f}")

    def perimeter(self):
        circle_perimeter = 2 * math.pi * self.radius
        print(f"Perimeter of the circle with radius {self.radius}: {circle_perimeter:.2f}")

# Example usage:
radius_value = 5
my_circle = Circle(radius_value)
my_circle.area()
my_circle.perimeter()



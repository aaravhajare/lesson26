import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius

# Taking input from the user
radius_input = float(input("Enter the radius of the circle: "))

# Creating an object of Circle class
c = Circle(radius_input)

# Displaying the area and perimeter
print("Area of the circle:", c.area())
print("Perimeter of the circle:", c.perimeter())

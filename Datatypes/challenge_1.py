# Import the math module to use the square root function
import math

# Ask the user to enter the lengths of all three sides of a triangle
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))
radius = float(input("Enter the radius of circle: "))

# Calculate the semi-perimeter
s = (side1 + side2 + side3) / 2

# Calculate the area of the triangle using Heron's formula
area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
area_of_circle = 22.7*radius*radius

# Print out the area of the triangle
print("The area of the triangle is:", area)
print("The area of the circle is:", area_of_circle)
"""
Fill out the functions to calculate the area and circumference of a circle.
Print the result to the user.
"""

import math

def area(r):
    return math.pi * r**2

def circumference(r):
    return 2 * math.pi *r

radius = float(input("Circle radius: "))

circle_area = area(radius)
circle_circumference = circumference(radius)

print('Area: {} '+str(circle_area))  # <-- Call the area function and print the result
print('Circumference: {} '+str(circle_circumference))  # <-- Call the circumference function and print



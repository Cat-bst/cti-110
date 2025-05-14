# Catherine Best
# 3/6/2025
# P2LAB1
# Circumference, area, and diameter

import math
radius = float(input("What is the radius of the circle? "))
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f"\nThe diameter of the circle is {diameter:.1f}")
print(f"\nThe circumference of the circle is {circumference:.2f}")
print(f"\nThe area of the circle is {area:.3f}")
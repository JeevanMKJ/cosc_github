"""
9. Write an IPO chart for a function called calc_circle_is_bigger_than_square
that receives as arguments the radius of a circle and the length of the side of a square.
The function should return three things: a Boolean that indicates whether the area of
the circle is greater than the area of the square and the areas of the two shapes.

10. Write the Python code that implements the calc_circle_is_bigger_than_square function
from the previous problem. Use the math module for math.pi.
"""
import math

def calc_circle_is_bigger_than_square(radius, square_length):

    area_circle = math.pi * (radius ** 2)
    square_area = square_length * 2
    print(f"Circle area: {area_circle:.2f}")
    print(f"Square area: {square_area:.2f}")

    if area_circle > square_area:
        circle_bigger = True
        print(f"Area of circle is larger than square area: {circle_bigger}")
    else:
        circle_bigger = False
        print(f"Area of circle is larger than square area: {circle_bigger}")

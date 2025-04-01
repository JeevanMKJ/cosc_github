"""
17. Write a function that receives degrees as an argument
and uses a function in the math module to convert degrees to radians.
It should return radians to the calling program.
"""

import math

def main():
    angle_degree = int(input("Enter angle in degrees: "))
    angle_radians = degree_to_radians(angle_degree)
    print(f"Ange in radians: {angle_radians:.2f}")


def degree_to_radians(degrees):
    return math.radians(degrees)

if __name__ == '__main__':
    main()
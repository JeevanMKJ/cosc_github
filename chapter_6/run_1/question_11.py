"""
11. Write the call to the previous function from main, passing a radius of 25 and
a length of 10 receiving the values returned from the function.
"""

from question_10 import calc_circle_is_bigger_than_square

def main():
    radius = 25
    square_length = 10
    calc_circle_is_bigger_than_square(radius, square_length)

if __name__ == '__main__':
    main()
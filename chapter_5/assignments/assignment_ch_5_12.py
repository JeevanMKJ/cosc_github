"""
When an object is falling because of gravity, the following formula
can be used to determine the distance the object falls in a specific time period:
d=1⁄2 * (gt ** 2)
The variables in the formula are as follows:
d is the distance in meters,
g is 9.8, and t is the amount of time,
in seconds, that the object has been falling.

Write a function named falling_distance that accepts an object’s
falling time (in seconds) as an argument. The function should return the distance,
in meters, that the object has fallen during that time interval.
Write a program that calls the function in a loop that passes
the values 1 through 10 as arguments and displays the return value.
"""

def main():
    print("Distance\tTime")
    print("----------------")

    for i in range(1, 11):
        meters = falling_distance(i)
        print(f"{meters:.2f}\t\t{i}")


def falling_distance(falling_time):
    gravity = 9.8
    constant = 0.5

    distance = constant * (gravity * (falling_time ** 2))
    return distance


if __name__ == '__main__':
    main()

# Author: Jeevan Morgan Kress-Jones
# Program Status: Complete
# This program calculates the distance an object covers in free fall over the time span of 10 seconds.

from distance import falling_distance

# The main function calls the falling_distance function in a for loop 10 times.
# For each iteration of the loop the distance of is calculated at time t and printed as well as t printed.
def main():

    MIN = 1
    MAX = 11

    print("\nTime\tFalling Distance")
    print("----------------------")

    for time_falling in range(MIN, MAX):
        print(f"{time_falling}\t\t{falling_distance(time_falling):.2f}")

if __name__ == '__main__':
    main()

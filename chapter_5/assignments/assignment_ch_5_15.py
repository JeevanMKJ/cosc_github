"""
In this chapter, you saw an example of how to write
an algorithm that determines whether a number is even or odd.
Write a program that generates 100 random numbers and keeps
a count of how many of those random numbers are even,
and how many of them are odd.
"""
import random

def main():
    rand_numbers = []

    for i in range(1, 101):
        random_num = random.randint(1, 100)
        rand_numbers.append(random_num)

        if rand_numbers[i - 1] % 2 == 0:
            print(f"{random_num}\t-\tEven")
        else:
            print(f"{random_num}\t-\tUneven")


if __name__ == '__main__':
    main()
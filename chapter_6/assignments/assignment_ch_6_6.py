"""
Assume a file containing a series of integers is
named numbers.txt and exists on the computer’s disk.
Write a program that calculates the average of all
the numbers stored in the file.
"""

def main():
    with open('random_numbers.txt', 'r') as num_file:
        num = num_file.readline()
        total = 0
        count = 0

        while num != '':
            num = int(num)
            total += num
            count += 1

            num = num_file.readline()

    num_average = total / count
    print(f"Number list average: {num_average:.2f}")


if __name__ == '__main__':
    main()
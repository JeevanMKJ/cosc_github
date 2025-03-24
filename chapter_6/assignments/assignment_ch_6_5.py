"""
Assume a file containing a series of integers is
named numbers.txt and exists on the computer’s disk.
Write a program that reads all of the numbers stored
in the file and calculates their total.
"""

def main():
    with open('../number_list.txt', 'r') as number_list:

        num = number_list.readline()
        total = 0

        while num != '':
            num = int(num)
            total += num
            print(f"{num}")

            num = number_list.readline()

    print(f"\nTotal of number list: {total}")

if __name__ == '__main__':
    main()
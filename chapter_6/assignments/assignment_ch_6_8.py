"""
This exercise assumes you have completed Programming Exercise 7, Random Number File Writer.
Write another program that reads the random numbers from the file,
displays the numbers, then displays the following data:
• The total of the numbers
• The number of random numbers read from the file
"""

def main():
    with open('random_numbers.txt', 'r') as num_list:
        num = num_list.readline()
        total = 0
        count = 0

        while num != '':
            num = int(num)
            total += num
            count += 1

            print(f"{num}")

            num = num_list.readline()

        print(f"\nNumber list sum: {total}")
        print(f"NUmber of rand numbers: {count}")


if __name__ == '__main__':
    main()
"""
Modify the program that you wrote for Exercise 6 so it handles the following exceptions:
• It should handle any IOError exceptions that are raised when the file is opened and
data is read from it.
• It should handle any ValueError exceptions that are raised when the
items that are read from the file are converted to a number.
"""

def main():
    try:
        with open('../number_list.txt', 'r') as num_file:
            num = num_file.readline()
            total = 0
            count = 0

            while num != '':
                num = int(num)
                total += num
                count += 1

                num = num_file.readline()

        num_average = total / count
        print(f"Number list average: {num_average:.1f}")
    except IOError:
        print("IOError: could not access file.")
    except ValueError as e:
        print(f"ValueError {e}")

if __name__ == '__main__':
    main()
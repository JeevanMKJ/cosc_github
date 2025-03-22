# Author: Jeevan Morgan Kress-Jones
# Program Status: Complete


def main():
    try:
        with open('number_list.txt', 'r') as number_file:

            num = number_file.readline()
            total = 0
            count = 0

            while num != '':
                num = float(num)
                total += num
                count += 1

                num = number_file.readline()

        list_average = total / count

        print(f"Number sum: {total:.2f}")
        print(f"Number average: {list_average:.2f}")
    except IOError:
        print(f"IOError: File can not be accessed.\nCheck if file name, pathing, permissions and mode are correct.")
    except ValueError as e:
        print(f"An error occurred at: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == '__main__':
    main()
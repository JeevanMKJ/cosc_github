# Author: Jeevan Morgan Kress-Jones
# Program Status: Complete

def main():
    random_number_file_reader()

def random_number_file_reader():
    try:
        num_list = open('../num_file.txt', 'r')
        num_sum = 0
        num_count = 0

        for line in num_list:
            try:
                num = int(line.strip('\n'))
                num_count += 1
                num_sum += num
                print(f"{num}")
            except ValueError:
                print(f"Warning: Invalid data '{line.strip()}' found in file - skipping.")

        num_list.close()

        print(f"Total of all random numbers: {num_sum}")
        print(f"Number of random numbers: {num_count}")

        if num_count > 0:
            average = num_sum / num_count
            print(f"Average of all random numbers: {average:.2f}")
        else:
            print("ERROR: The number of random numbers needs to be larger than 0.")

    except IOError:
        print("ERROR: Could not read from file. Make sure num_file.txt exists.")
    except Exception as e:
        print(f"ERROR: An unexpected error occurred: {e}")


if __name__ == '__main__':
    main()
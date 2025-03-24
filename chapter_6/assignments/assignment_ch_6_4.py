"""
Assume a file containing a series of names (as strings) is named
names.txt and exists on the computer’s disk.
Write a program that displays the number of names that are stored in the file.
(Hint: Open the file and read every string stored in it.
Use a variable to keep a count of the number of items that are read from the file.)
"""

def main():
    with open('name_list.txt', 'r') as name_file:

        line = name_file.readline()
        count = 0

        while line != '':
            count += 1
            line = name_file.readline()

    print(f"Number of names in list: {count}")

if __name__ == '__main__':
    main()
# Author: Jeevan Morgan Kress-Jones
# Program Status: Complete
# This program reads the file text.txt and returns the count of
# Uppercase letters, Lowercase letters, Digits and Spaces

def main():
    text = read_text_file()
    print(text)
    find_char_count(text)

def read_text_file():
    with open('text.txt', 'r') as text_file:
        text = text_file.read()
    return text

def find_char_count(text):
    count_upper = 0
    count_lower = 0
    count_digit = 0
    count_space = 0
    for char in text:
        if char.isupper():
            count_upper += 1
        if char.islower():
            count_lower += 1
        if char.isdigit():
            count_digit += 1
        if char.isspace():
            count_space += 1
    print(f"Uppercase letters: {count_upper}")
    print(f"Lowercase letters: {count_lower}")
    print(f"Digits: {count_digit}")
    print(f"Whitespaces: {count_space}")

if __name__ == '__main__':
    main()
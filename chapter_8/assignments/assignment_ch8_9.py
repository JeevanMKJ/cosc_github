"""
9. Vowels and Consonants
Write a program with a function that accepts a string as an argument
and returns the number of vowels that the string contains.
The application should have another function that accepts
a string as an argument and returns the number of consonants
that the string contains.
The application should let the user enter a string,
and should display the number of vowels and the number
of consonants it contains.
"""

def main():
    user_string = user_input()

    char_string = ''

    for ch in user_string:
        if ch.isalpha():
            char_string += ch

    vowel_count = filter_vowels(char_string)
    filter_consonants(char_string, vowel_count)

def user_input():
    print("--Filter vowels and consonants--")
    #user_string = input("Enter string: ")
    user_string = "I wandered lonely as a cloud. That floats on high o'er vales and hills. When all at once I saw a crowd. A host, of golden daffodils. Beside the lake, beneath the trees. Fluttering and dancing in the breeze."
    return user_string

def filter_vowels(string):
    count_a = 0
    count_e = 0
    count_i = 0
    count_o = 0
    count_u = 0
    for i in string:
        if i == "a" or i == "A":
            count_a += 1
        if i == "e" or i == "E":
            count_e += 1
        if i == "i" or i == "I":
            count_i += 1
        if i == "o" or i == "O":
            count_o += 1
        if i == "u" or i == "U":
            count_u += 1
    total_count = count_a + count_e + count_i + count_o + count_u
    print(f"Vowel count: {total_count}")
    return total_count

def filter_consonants(string, vowel_count):
    consonant_count = len(string) - vowel_count
    print(f"Consonant count: {consonant_count}")
    return consonant_count

if __name__ == '__main__':
    main()
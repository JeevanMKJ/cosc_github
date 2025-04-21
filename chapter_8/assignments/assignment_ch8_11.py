"""
11. Word Separator
Write a program that accepts as input a sentence
in which all of the words are run together,
but the first character of each word is uppercase.
Convert the sentence to a string in which the words
are separated by spaces,
and only the first word starts with an uppercase letter.
For example the string “StopAndSmellTheRoses.”
would be converted to “Stop and smell the roses.”
"""

def main():
    sentence = user_input()
    print(sentence)
    insert_spaces(sentence)

def user_input():
    print("--Enter run together sentence--")
    while True:
        #user_sentence = input("Enter sentence: ")
        user_sentence = "StopAndSmellTheRoses"
        if any(char.isspace() for char in user_sentence):
            print("ERROR: No spaces.")
        else:
            return user_sentence

def insert_spaces(sentence):
    spaced_sentence = ""
    for char in sentence:
        if char.islower() and (char + 1).isupper():
            print("Yes")


if __name__ == '__main__':
    main()
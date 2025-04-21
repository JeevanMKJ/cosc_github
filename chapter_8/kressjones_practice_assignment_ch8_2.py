# Author: Jeevan Morgan Kress-Jones
# Program Status: Complete
# This program takes in sentence and returns the original
# sentence as well as newly formatted sentence.
# The formatted sentence flips all lowercase letters
# to uppercase and uppercase letters to lowercase.

def main():
   sentence = process_user_input()
   flipped_sentence = flip_sentence(sentence)
   print(f"Original sentence: {sentence}")
   print(f"Flipped sentence: {flipped_sentence}")

def process_user_input():
    while True:
        sentence = input("Enter sentence (or type 'exit' to quit): ")
        if not sentence or sentence == " ":
            print("ERROR: Input can not be empty.")
            continue
        if sentence.lower() == "exit":
            print("Good Bye")
            exit()
        if input_validation(sentence):
            break
        else:
            print("ERROR: Only enter letters and special characters.")
    return sentence

def input_validation(sentence):
    accepted_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    for char in sentence:
        if char not in accepted_characters:
            print(f"ERROR: Invalid input: {char}")
            return False
    return True

def flip_sentence(sentence):
    lower_letters = "abcdefghijklmnopqrstuvwxyz"
    upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    flipped_sentence = ""
    for char in sentence:
        if char in upper_letters:
            flipped_sentence += char.lower()
        elif char in lower_letters:
            flipped_sentence += char.upper()
        else:
            flipped_sentence += char
    return flipped_sentence

if __name__ == '__main__':
    main()
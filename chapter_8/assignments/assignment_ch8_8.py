"""
8. Sentence Capitalizer
Write a program with a function that accepts a string
as an argument and returns a copy of the string with
the first character of each sentence capitalized.
For instance, if the argument is
“hello. my name is Joe. what is your name?”
the function should return the string
“Hello. My name is Joe. What is your name?”
The program should let the user enter
a string and then pass it to the function.
The modified string should be displayed.
"""

def main():
    sentence_list = user_input()
    string_list = []

    for i in range(len(sentence_list)):
        if sentence_list[i][0] == ' ':
            sentence_list[i] = sentence_list[i].lstrip()

    for string in sentence_list:
        updated_string = string.replace(string[0], string[0].upper(), 1)
        string_list.append(updated_string)

    sentence = ''
    for string in string_list:
        sentence += string + '. '
    final_sentence = sentence[:-2]
    print(final_sentence)

def user_input():
    user_sentence = "hello. my name is Jay. what is your name?"
    sentence = user_sentence.split('.')
    print(sentence)
    return sentence

if __name__ == '__main__':
    main()
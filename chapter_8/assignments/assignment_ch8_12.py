"""
12. Pig Latin
Write a program that accepts a sentence as input
and converts each word to “Pig Latin.”
In one version, to convert a word to Pig Latin,
you remove the first letter and place that letter
at the end of the word.
Then, you append the string “ay” to the word. Here is an example:
English: I SLEPT MOST OF THE NIGHT
Pig Latin: IAY LEPTSAY OSTMAY FOAY HETAY IGHTNAY
"""

def main():
    sentence = user_input()
    print(sentence)
    convert_sentence(sentence)

def user_input():
    print("--Create a 'Pig Latin' sentence--")
    while True:
        #sentence = input("Enter sentence: ")
        user_sentence = "Hi name is Bill."
        if any(char.isdigit() for char in user_sentence):
            print("ERROR: Only use letters.")
        else:
            sentence = user_sentence.replace(".", "")
            return sentence.upper()

def convert_sentence(sentence):
    tokens = sentence.split(' ')
    pig_latin_sentence = ""
    for word in tokens:
        if word:
            pig_latin = word[1:] + word[0] + "AY"
            pig_latin_sentence += pig_latin + " "
    pig_latin_sentence = pig_latin_sentence.rstrip() + "."
    print(pig_latin_sentence)

if __name__ == '__main__':
    main()
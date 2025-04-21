"""
10. Most Frequent Character
Write a program that lets the user enter
a string and displays the character that
appears most frequently in the string.
"""

def main():
    sentence = user_input()
    find_most_freq_char(sentence)

def user_input():
    #sentence = input("Enter string: ")
    sentence = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque hendrerit feugiat nulla sed imperdiet. Donec sed sapien blandit, malesuada ex quis, interdum lorem."
    return sentence

def find_most_freq_char(string):
    most_frequent = max(set(string), key=string.count)
    print(most_frequent)

if __name__ == '__main__':
    main()
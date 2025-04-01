"""
12. Write code that opens an output file with the filename numberList.txt but
does not erase the file’s contents if it already exists.
"""

with open('numberList.txt', 'a') as infile:
    content = infile.read()
    infile.close()

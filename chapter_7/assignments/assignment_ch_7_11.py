"""
11. Lo Shu Magic Square
The Lo Shu Magic Square is a grid with 3 rows and 3 columns,
shown in Figure 7-23. The Lo Shu Magic Square has the following properties:

• The grid contains the numbers 1 through 9 exactly.
• The sum of each row, each column, and each diagonal all add up to the same number.

In a program you can simulate a magic square using a two-dimensional list.
Write a function that accepts a two-dimensional list as an argument and
determines whether the list is a Lo Shu Magic Square. Test the function in a program.
"""
import random

def main():
    gms = generated_magic_square()
    magic_square_total = 45
    compare_lists(gms, magic_square_total)

def compare_lists(gms_list, mst):
    gmt_total = 0
    for r in range(3):
        for c in range(3):
            gmt_total += gms_list[r][c]
    if gmt_total == mst:
        gmt_equal_mst = True
        print(f"Generated magic square is equal to Lo Shu's magic square: {gmt_equal_mst}")
    else:
        gmt_equal_mst = False
        print(f"Generated magic square is equal to Lo Shu's magic square: {gmt_equal_mst}")

def generated_magic_square():
    rows = 3
    cols = 3
    gms = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0],]
    for r in range(rows):
        for c in range(cols):
            gms[r][c] = random.randint(1, 10)
    print(gms)
    return gms

if __name__ == '__main__':
    main()
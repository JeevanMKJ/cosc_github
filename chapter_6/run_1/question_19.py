"""
19. Write a loop that calculates the total of the following series of numbers:

1/30   + 2/29   +    3/28   . . . . + 30/1
"""

"""
num_top = 1
num_bottom = 30
total = 0

for i in range(1, 31):
    division = num_top / num_bottom
    num_top += 1
    num_bottom -= 1
    print(f"{division:.5f}")
    total += division
print(f"Sum: {total:.2f}")
"""

#OR

total = 0

for numerator in range(1, 31):
    denominator = 31 - numerator
    total += numerator / denominator
print(f"Sum: {total:.2f}")




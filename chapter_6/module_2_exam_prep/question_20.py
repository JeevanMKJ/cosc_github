"""
20. Write the statements needed to randomly select a number
from the following sequence:  0, 5, 10, 15, 20, 25, 30.
"""

import random

random_num = random.randrange(0, 30, 5)
print(random_num)
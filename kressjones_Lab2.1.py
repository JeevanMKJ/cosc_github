#Author: Jeevan Morgan Kress-Jones
#Program Status: Complete ✅
#Based on the users inputs, this programs calculates the required ingredient amounts for a spaghetti-sauce recipie for the desired serving number.

#IPO Diagram
"""
| Input                           | Processing                              | Output                                |
|---------------------------------|-----------------------------------------|---------------------------------------|
| Number of desired servings      | Calculate required ingredient amounts   | Display required ingredient amounts   |
"""

INGREDIENT_TOMATO_SAUCE = 2.0 #in cups
INGREDIENT_TOMATO_PASTE = 0.333 #in cups
INGREDIENT_GARLIC = 2 #cloves
INGREDIENT_OREGANO = 1 #tbsp

desired_servings = float(input("Enter the desired serving amount: "))

required_tomato_sauce = (desired_servings / 4) * INGREDIENT_TOMATO_SAUCE
required_tomato_paste = (desired_servings / 4) * INGREDIENT_TOMATO_PASTE
required_garlic = (desired_servings / 4) * INGREDIENT_GARLIC
required_oregano = (desired_servings / 4) * INGREDIENT_OREGANO

print(f"For {desired_servings:,.1f} servings of spaghetti sauce, you will need:")
print(f"Tomato Sauce: {required_tomato_sauce:,.2f} cups")
print(f"Tomato Paste: {required_tomato_paste:,.2f} cups")
print(f"Garlic: {required_garlic:,.2f} cloves")
print(f"Oregano: {required_oregano:,.2f} tbsp")

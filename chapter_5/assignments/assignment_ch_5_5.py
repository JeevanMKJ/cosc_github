"""
A county collects property taxes on the assessment value of property,
which is 60 percent of the property’s actual value.
For example, if an acre of land is valued at $10,000, its assessment value is $6,000.
The property tax is then 72¢ for each $100 of the assessment value.
The tax for the acre assessed at $6,000 will be $43.20. Write a program
that asks for the actual value of a piece of property and
displays the assessment value and property tax.
"""

def main():
    assessment_value_percentage = 0.6
    tax_per_100_usd = 0.72 / 100

    while True:
        property_value = input("Enter properties total value in USD: ")

        if property_value.isdigit():
            property_value = float(property_value)
            break
        else:
            print("ERROR. Enter number.")

    assessment_value = property_value * assessment_value_percentage

    property_tax = assessment_value  * tax_per_100_usd

    print(f"The assessment value for your ${property_value:,.2f} valued property is: ${assessment_value:.2f}")
    print(f"The property tax for your ${property_value:,.2f} valued property is: ${property_tax:.2f}")


if __name__ == '__main__':
    main()
# IPO Diagram
"""
| Input                         | Output                           | Output                          |
|-------------------------------|----------------------------------|---------------------------------|
| Monthly Gross Income          | Accept Input from user           | Display net monthly income      |
| Monthly Paycheck Deductions   | Accept Input from user           | Display yearly gross income     |
                                | Calculate net monthly income     | Display yearly gross income     | 
                                | Calculate yearly gross income    |                                 |
                                | Calculate yearly net income      |                                 |
"""

gross_income = float(input("Enter gross monthly income: " ))
deductions = float(input("Enter monthly paycheck deductions: "))

monthly_net_income = gross_income - deductions
yearly_gross_income = gross_income * 12
yearly_net_income = monthly_net_income * 12

print(f"Here is a break-down of your monthly and annual finances:")
print(f"| Description         | value in USD")
print(f"|---------------------|------------------------")
print(f"| Monthly net income  | ${monthly_net_income:,.2f}")
print(f"| Yearly gross income | ${yearly_net_income:,.2f}")
print(f"| Yearly net income   | ${yearly_net_income:,.2f}")

annual_income = float(input("Enter your annual income: "))
age = int(input("Enter your age: "))
investment = float(input("Enter your Investment Amount: "))

if age>=60:
    print(f"\nSenior Citizen Exemption Applicable")

if annual_income < 500000:
    tax_amount = 0
    print(f"\nTax Status: No Tax Applicable")
    print(f"Tax Amount: {tax_amount}")

elif annual_income <= 1000000:
    tax_amount = annual_income * 0.1
    print(f"\nTax Status: Tax Applicable")
    print(f"Tax Amount: {tax_amount}")

elif annual_income <= 2000000:
    tax_amount = annual_income * 0.2
    print(f"\nTax Status: Tax Applicable")
    print(f"Tax Amount: {tax_amount}")  

else:
    tax_amount = annual_income * 0.3
    print(f"\nTax Status: Tax Applicable")
    print(f"Tax Amount: {tax_amount}")

tax_amount_after_investment = tax_amount - investment

if tax_amount_after_investment < 0:
    tax_amount_after_investment = 0

print(f"\nTax Amount after Investment: {tax_amount_after_investment}")
print(f"Annual Income: {annual_income}")
print(f"Investment Amount: {investment}")
print(f"Final Tax Amount: {tax_amount_after_investment}")
print("Thank you for using the Income Tax Calculator!")
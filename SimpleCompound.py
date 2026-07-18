principle = float(input("Enter the principle amount : "))
rate = float(input("Enter the rate of interest :"))
time = float(input("Enter the time in years :"))
simple_interest = (principle*rate*time)/100
print(f"The Simple Interest is : {simple_interest}")
compound_interest = principle * (1 + rate/100) ** time - principle
print(f"The Compound Interest is : {compound_interest}")



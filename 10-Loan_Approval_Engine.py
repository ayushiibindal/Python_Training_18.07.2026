salary = float(input("Enter your monthly salary: "))
credit_score = int(input("Enter your credit score: "))
existing_loan = float(input("Enter your existing Loan Amount: "))
employment = input("Enter your Employment Type (employed/self-employed/unemployed): ").lower()

if salary>80000 and credit_score > 750 and existing_loan < 20000:
    print("f\nLoan Status: Approved Immediately")
    print(f"Employment Type: {employment}")

elif salary>50000 and credit_score>650:
    print(f"\nLoan Status: Approved with Caution")
    print(f"Employment Type: {employment}")

elif credit_score<600:
    print(f"\nLoan Status: Rejected")
    print(f"Reason: Credit score is below 600")

else:
    print(f"\nLoan Status: Manual Review Required")
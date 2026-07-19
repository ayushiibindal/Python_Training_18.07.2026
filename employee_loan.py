# Employee Loan Eligibility System

name = input("Enter applicant name : ")
age = int(input("Enter age : "))
monthly_salary = int(input("Enter monthly salary : "))
experience = int(input("Enter work experience in years : "))
credit_score = int(input("Enter credit score : "))
existing_emi = int(input("Enter existing monthly EMI : "))

if age >= 21 and age <= 58 and experience >= 2 and  credit_score >= 650:
    if existing_emi <= 0.4 * monthly_salary:
        if monthly_salary >= 25000 and monthly_salary <= 39999:
            max_loan = "₹2,00,000"
        elif monthly_salary >= 40000 and monthly_salary <= 59999:
            max_loan = "₹5,00,000"
        elif monthly_salary >= 60000 and monthly_salary <= 99999:
            max_loan = "₹10,00,000"
        elif monthly_salary >= 100000:
            max_loan = "₹15,00,000"
        else:
            print("Loan Application Status: Rejected")
            print("Reason: Monthly salary is below ₹25,000.")
            exit()
        
        print("\nApplicant Name:", name)
        print("Loan Application Status: Eligible")
        print("Maximum Loan Amount:", max_loan)



#git init, add, commit

#type nul> file name.py






name = input("Enter applicant name: ")
age = int(input("Enter age: "))
monthly_salary = int(input("Enter monthly salary: "))
work_experience = int(input("Enter work experience in years: "))
credit_score = int(input("Enter credit score: "))
existing_emi = int(input("Enter existing monthly EMI: "))

# Initialize eligibility status
is_eligible = True
rejection_reason = ""

# Check age requirement
if age < 21 or age > 58:
    is_eligible = False
    rejection_reason = "Age must be between 21 and 58 years."
# Check work experience requirement
elif work_experience < 2:
    is_eligible = False
    rejection_reason = "Work experience must be at least 2 years."
# Check credit score requirement
elif credit_score < 650:
    is_eligible = False
    rejection_reason = "Credit score is below 650."
# Check EMI requirement
elif existing_emi > (0.4 * monthly_salary):
    is_eligible = False
    rejection_reason = "Existing monthly EMI exceeds 40% of monthly salary."

# Determine loan amount based on salary
if is_eligible:
    if monthly_salary >= 25000 and monthly_salary <= 39999:
        max_loan = "₹2,00,000"
    elif monthly_salary >= 40000 and monthly_salary <= 59999:
        max_loan = "₹5,00,000"
    elif monthly_salary >= 60000 and monthly_salary <= 99999:
        max_loan = "₹10,00,000"
    elif monthly_salary >= 100000:
        max_loan = "₹15,00,000"
    else:
        is_eligible = False
        rejection_reason = "Monthly salary is below ₹25,000."

# Display results
print("\nApplicant Name:", name)

if is_eligible:
    print("Loan Application Status: Eligible")
    print("Maximum Loan Amount:", max_loan)
else:
    print("Loan Application Status: Rejected")
    print("Reason:", rejection_reason)
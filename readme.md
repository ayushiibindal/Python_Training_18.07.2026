# Employee Loan Eligibility System

A simple Python project developed to determine whether a working professional is eligible for a personal loan based on predefined banking rules.

This project is ideal for beginners to practice:
- Python Basics
- User Input
- if-elif-else Decision Making
- Conditional Statements
- Arithmetic Operations
- Input Validation
- Clean Code Structure

---

## Problem Statement

A bank wants to automate the loan eligibility process for working professionals.

The application checks an applicant's eligibility based on:

- Applicant's Age
- Monthly Salary
- Work Experience
- Credit Score
- Existing Monthly EMI

If all eligibility conditions are satisfied, the system displays the maximum loan amount the applicant is eligible for. Otherwise, it rejects the application with an appropriate reason.

---

## Eligibility Rules

### Age
- Applicant must be between **21 and 58 years**.

### Work Experience
- Minimum **2 years** of work experience.

### Credit Score
- Credit score must be **650 or above**.

### Monthly Salary & Loan Eligibility

| Monthly Salary | Maximum Loan Amount |
|----------------|---------------------|
| ₹25,000 – ₹39,999 | ₹2,00,000 |
| ₹40,000 – ₹59,999 | ₹5,00,000 |
| ₹60,000 – ₹99,999 | ₹10,00,000 |
| ₹1,00,000 and above | ₹15,00,000 |

### EMI Rule

- Existing monthly EMI should **not exceed 40%** of the applicant's monthly salary.

---

## Features

- Accepts applicant details from the user.
- Validates age eligibility.
- Checks minimum work experience.
- Verifies credit score.
- Calculates EMI eligibility.
- Determines maximum loan amount based on salary.
- Displays appropriate rejection reason if any condition fails.
- Simple and beginner-friendly implementation using `if-elif-else`.

---

## Expected Input

```text
Enter applicant name:
Enter age:
Enter monthly salary:
Enter work experience in years:
Enter credit score:
Enter existing monthly EMI:
```

---

## Sample Output (Eligible)

```text
Applicant Name: Rahul Sharma

Loan Application Status: Eligible

Maximum Loan Amount: ₹5,00,000
```

---

## Sample Output (Rejected)

```text
Applicant Name: Rahul Sharma

Loan Application Status: Rejected

Reason: Credit score is below 650.
```

---

## Technologies Used

- Python 3
- Conditional Statements (`if-elif-else`)
- User Input
- Arithmetic Operators
- Comparison Operators

---

## Project Structure

```
Employee-Loan-Eligibility-System/
│
├── employee_loan.py
├── README.md
```

---

## Learning Outcomes

By completing this project, you will learn:

- Working with user input
- Writing decision-making logic
- Using nested `if-elif-else`
- Implementing real-world business rules
- Writing clean and readable Python programs

---

## Future Enhancements

- GUI using Tkinter
- Database integration (MySQL)
- Loan EMI Calculator
- Interest Rate Calculation
- File Handling for Applicant Records
- Streamlit Web Application
- Exception Handling and Input Validation

---

## Author

**Ayushi Bindal**

Python Training Project

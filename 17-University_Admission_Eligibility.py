entrance_score = int(input("Enter Entrance Exam Score: "))
percentage = float(input("Enter 12th Percentage: "))
category = input("Enter Category (general/reserved): ").lower()
extra_score = int(input("Enter Extracurricular Score: "))

if entrance_score >= 90 and percentage >= 85:
    print(f"\nAdmission Status: Direct Admission")

elif category == "reserved" and entrance_score >= 80:
    print(f"\nAdmission Status: Direct Admission with Relaxation")

elif entrance_score >= 70 and extra_score >= 8:
    print(f"\nAdmission Status: Waitlisted")

else:
    print(f"\nAdmission Status: Rejected")
    print("Reason: Entrance score or percentage not sufficient for admission.")

    
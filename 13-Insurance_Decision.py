age = int(input("Enter Customer Age: "))
smoking = input("Smoking Habit (yes/no): ").lower()
BMI = float(input("Enter BMI: "))
disease = input("Pre-existing Disease (yes/no): ").lower()

if disease == "yes" and age > 60:
    print(f"\nInsurance Status: Rejected")

elif smoking == "yes" and age > 50:
    print(f"\nPremium Type: High Premium")

elif BMI > 25:
    print(f"\nPremium Type: Medium Premium")

elif age < 40 and smoking == "no" and disease == "no" and BMI <= 25:
    print(f"\nPremium Type: Low Premium")

else:
    print(f"\nPremium Type: Standard Premium")
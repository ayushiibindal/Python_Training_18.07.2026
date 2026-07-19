employee_name = input("Enter Employee Name: ")
rating = float(input("Enter Employee Rating (1-5): "))
experience = int(input("Enter Employee Experience in years: "))
delivery_status = input("Enter Project Delivery Status (on time/delayed): ").lower()

if rating == 5 and experience > 10 and delivery_status == "on time":
    print(f"\nEmployee {employee_name} is eligible for bonus.")
    print("Bonus Awarded : 30%")

elif rating == 4 and experience>7:
    print(f"\nEmployee {employee_name} is eligible for bonus.")
    print("Bonus Awarded : 20%")

elif rating == 3 and delivery_status == "dealayed":
    print(f"\nEmployee {employee_name} is eligible for bonus.")
    print("Bonus Awarded : 5%")

else:
    print(f"\nEmployee {employee_name} is not eligible for bonus.")
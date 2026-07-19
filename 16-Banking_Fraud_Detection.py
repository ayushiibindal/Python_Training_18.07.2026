transaction_amount = float(input("Enter Transaction Amount: ₹"))
location_mismatch = input("Location Mismatch (yes/no): ").lower()
login_time = input("Unusual Login Time (yes/no): ").lower()
account_age = int(input("Enter Account Age (in months): "))
unusual_activity = input("Repeated Unusual Activity (yes/no): ").lower()

if transaction_amount > 100000 and location_mismatch == "yes":
    print(f"\nTransaction Status: Fraud Alert")

elif account_age < 6 and login_time == "yes":
    print(f"\nTransaction Status: Risk Alert")

elif transaction_amount > 50000 and unusual_activity == "yes":
    print(f"\nTransaction Status: Manual Review")

else:
    print(f"\nTransaction Status: Approved")
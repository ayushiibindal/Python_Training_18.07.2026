compute_hours = int(input("Enter Compute Hours: "))
storage = int(input("Enter Storage Used (GB): "))
support_plan = input("Enter Support Plan (basic/premium/enterprise): ").lower()

# Rates
compute_rate = 10
storage_rate = 2

if support_plan == "basic":
    support_fee = 500
    compute_cost = compute_hours * compute_rate

elif support_plan == "premium":
    support_fee = 1000
    compute_cost = compute_hours * 8      # Discounted rate

elif support_plan == "enterprise":
    support_fee = 2000
    compute_cost = compute_hours * 7      # Custom rate
    storage_rate = 1                      # Storage discount

else:
    print("Invalid Support Plan")
    exit()

storage_cost = storage * storage_rate
total_bill = compute_cost + storage_cost + support_fee

print(f"\nSupport Plan: {support_plan.title()}")
print(f"Compute Cost: ₹{compute_cost}")
print(f"Storage Cost: ₹{storage_cost}")
print(f"Support Fee: ₹{support_fee}")
print(f"Final Bill: ₹{total_bill}")
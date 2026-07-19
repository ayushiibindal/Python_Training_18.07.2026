monthly_usage = int(input("Enter Monthly Usage (hours): "))
missed_payments = int(input("Enter Number of Missed Payments: "))
support_tickets = int(input("Enter Number of Support Tickets: "))
satisfaction = int(input("Enter Satisfaction Score (1-10): "))

if monthly_usage > 100 and satisfaction >= 8:
    print(f"\nRenewal Prediction: Likely to Renew")

elif monthly_usage < 50 and support_tickets > 5:
    print(f"\nRenewal Prediction: High Churn Risk")

elif missed_payments > 2:
    print(f"\nRenewal Prediction: Payment Risk")

else:
    print(f"\nRenewal Prediction: Moderate Renewal Probability")
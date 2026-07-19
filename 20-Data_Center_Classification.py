power = int(input("Enter Total Power Consumption (kW): "))
cooling = input("Enter Cooling Efficiency (good/poor): ").lower()
rack_load = int(input("Enter Rack Load Percentage (%): "))

if power > 1000 and cooling == "poor":
    print(f"\nStatus: Critical")
    print(f"Reason: High Power Consumption and Poor Cooling")

elif rack_load > 85:
    print(f"\nStatus: Warning")
    print(f"Reason: Rack Load Exceeds Safe Limit")

elif cooling == "good" and rack_load <= 85:
    print(f"\nStatus: Normal")
    print(f"Reason: Cooling is Efficient and Rack Load is Within Safe Limit")

else:
    print(f"\nStatus: Moderate Risk")
    print(f"Reason: Power Consumption is Moderate but Cooling Efficiency is Poor")
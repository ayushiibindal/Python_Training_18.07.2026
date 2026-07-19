cpu = int(input("Enter CPU Usage (%): "))
memory = int(input("Enter Memory Usage (%): "))
disk = int(input("Enter Disk Usage (%): "))
latency = int(input("Enter Network Latency (ms): "))

if cpu > 90 and memory > 85:
    print(f"\nServer Status: Critical Alert")

elif disk > 95:
    print(f"\nServer Status: Storage Critical")

elif latency > 100:
    print(f"\nServer Status: Network Issue")

elif cpu > 70 or memory > 70 or disk > 80:
    print(f"\nServer Status: Warning")

else:
    print(f"\nServer Status: Healthy")
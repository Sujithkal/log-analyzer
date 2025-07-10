# Step 1: Create sample log data
sample_logs = """
2023-10-01 10:01:15 ERROR Failed login attempt from IP 192.168.1.20
2023-10-01 10:02:10 ERROR Failed login attempt from IP 192.168.1.20
2023-10-01 10:03:05 ERROR Failed login attempt from IP 192.168.1.20
2023-10-01 10:04:00 INFO User login successful from IP 192.168.1.30
2023-10-01 10:05:45 ERROR Failed login attempt from IP 192.168.1.40
2023-10-01 10:06:30 ERROR Failed login attempt from IP 192.168.1.40
2023-10-01 10:07:15 ERROR Failed login attempt from IP 192.168.1.50
2023-10-01 10:08:00 INFO User login successful from IP 192.168.1.50
2023-10-01 10:09:45 ERROR Failed login attempt from IP 192.168.1.40
"""

# Step 2: Save sample logs to a file
with open("sample_logs.txt", "w") as f:
    f.write(sample_logs.strip())

# Step 3: Define the log analyzer function
def analyze_logs(log_file, threshold=3):
    failed_attempts = {}

    with open(log_file, "r") as f:
        for line in f:
            if "ERROR Failed login attempt from IP" in line:
                ip = line.strip().split()[-1]
                failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

    # Identify suspicious IPs
    suspicious_ips = {ip: count for ip, count in failed_attempts.items() if count >= threshold}

    # Print report
    print("Suspicious IP Report:")
    print("----------------------")
    if suspicious_ips:
        for ip, count in suspicious_ips.items():
            print(f"IP Address: {ip} | Failed Attempts: {count}")
    else:
        print("No suspicious IPs detected.")

# Step 4: Run the analyzer
analyze_logs("sample_logs.txt")

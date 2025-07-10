# 🔍 Log Analyzer for Suspicious Activity

## 📄 Project Overview
This Python script analyzes system log files to detect suspicious activity, specifically multiple failed login attempts from the same IP address. It's a lightweight tool that simulates a basic SOC task and is perfect for showcasing your cybersecurity skills.

## 🚀 Features
- Parses log files for failed login attempts
- Flags IPs with repeated failures (default threshold: 3)
- Generates a report of suspicious IPs
- Easy to customize and extend

## 🧪 Sample Log Format
2023-10-01 10:01:15 ERROR Failed login attempt from IP 192.168.1.20
2023-10-01 10:04:00 INFO User login successful from IP 192.168.1.30

## 🛠️ How to Use
1. Run the code cell to generate the log file and analyze it.
2. The script will print a report of suspicious IPs directly in the output.

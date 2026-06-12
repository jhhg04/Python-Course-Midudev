import re
import time
from datetime import datetime
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

# ===== FUNCTIONS =====

# Read log file
def read_log_file(path):

    with open(path, "r") as file:
        return file.readlines()


# Find errors using regex 
def find_errors(lines):
    
    errors = []

    for line in lines:

        # Ignore uppercase/lowercase
        if re.search(r"ERROR|WARNING|500|timeout|CRITICAL", line, re.IGNORECASE):

            errors.append(line.strip())

    return errors


# Count error types
def count_error_types(errors):

    error_count = {
        "ERROR": 0,
        "WARNING": 0,
        "500": 0,
        "timeout": 0,
        "CRITICAL": 0
    }

    for error in errors:

        if "ERROR" in error.upper():
            error_count["ERROR"] += 1

        if "WARNING" in error.upper():
            error_count["WARNING"] += 1

        if "500" in error:
            error_count["500"] += 1

        if "TIMEOUT" in error.upper():
            error_count["timeout"] += 1

        if "CRITICAL" in error.upper():
            error_count["CRITICAL"] += 1  

    return error_count


# Detect IP addresses
def detect_ips(lines):

    ip_pattern = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"

    ips_found = []

    for line in lines:

        matches = re.findall(ip_pattern, line)

        for ip in matches:
            ips_found.append(ip)

    return ips_found


# Save report to file
def save_report(errors, error_summary, ips):

    with open("report.txt", "w") as report:

        report.write("===== LOG REPORT =====\n\n")

        report.write("Detected Issues:\n")

        for error in errors:
            report.write(error + "\n")

        report.write("\n===== ERROR SUMMARY =====\n")

        for key, value in error_summary.items():
            report.write(f"{key}: {value}\n")

        report.write("\n===== DETECTED IPs =====\n")

        for ip in ips:
            report.write(ip + "\n")

            
# Print summary to console
def print_summary(errors, error_summary, ips):

    print("\n===== LOG SUMMARY =====")

    current_time = datetime.now()

    if len(errors) == 0:
        print("No issues found")
    else:
        print(f"Total issues found: {len(errors)}")

        for error in errors:
            print(f"- {error}")


# ===== MAIN =====            

log_path = input("Enter log file path: ")

try:

    log_lines = read_log_file(log_path)

    detected_errors = find_errors(log_lines)

    print_summary(detected_errors)

except FileNotFoundError:    
    print("Log file not found")
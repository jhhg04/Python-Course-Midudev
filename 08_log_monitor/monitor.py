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

    return error_count

def print_summary(errors):

    print("\n===== LOG SUMMARY =====")

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
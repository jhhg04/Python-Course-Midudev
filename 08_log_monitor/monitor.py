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

  
def find_errors(lines):
    errors = []

    for line in lines:

        # Regex search
        if re.search(r"ERROR|WARNING|500|timeout", line):
            errors.append(line.strip())

    return errors


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
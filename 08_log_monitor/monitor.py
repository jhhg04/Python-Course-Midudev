import re

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
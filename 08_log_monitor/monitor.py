import re

def read_log_file(path):
    with open(path, "r") as file:
        return file.readlines()
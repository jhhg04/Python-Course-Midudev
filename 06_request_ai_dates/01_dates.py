# Working with dates and times in Python

from datetime import datetime, timedelta
import locale

# 1. Get the current date and time
now = datetime.now()
print(f"Current date and time: {now}") # Current date and time: 2026-03-31 22:30:33.157100

# 2. Create a specific date and time
specific_date = datetime(2025, 2, 12, 15, 30, 0)
print(f"Specific date and time: {specific_date}") # Specific date and time: 2025-02-12 15:30:00

# 3. Format dates
# strftime() method to format dates
# pass the datetime object and the specified format
# format:
import locale
locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')

formatted_date = now.strftime("%A %B %Y %H:%M:%S")
print(f"Formatted date: {formatted_date}") # Formatted date: Tuesday March 2026 22:30:33

# 4. Date operations (add/subtract days, minutes, hours, months)
yesterday = datetime.now() - timedelta(days=1)
print(f"Yesterday: {yesterday}") # Yesterday: 2026-03-31 22:51:28.985075

tomorrow = datetime.now() + timedelta(days=1)
print(f"Tomorrow: {tomorrow}")

one_hour_after = datetime.now() + timedelta(hours=1)
print(f"One hour later: {one_hour_after}")

# 5. Get individual components of a date
year = now.year
print(year)

month = now.month
print(month)

# 6. Calculate the difference between 2 dates
date1 = datetime.now()
date2 = datetime(2025, 2, 12, 15, 30, 0)
difference = date2 - date1
print(f"Difference between the dates: {difference}")
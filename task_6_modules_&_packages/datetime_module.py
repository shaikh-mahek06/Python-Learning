
from datetime import datetime
# 1. Current Date and Time
print(" 1. Current Date and Time")
now=datetime.now()
print(now)

# 2. Current Date
print("2. Current Date")
today=datetime.now()
print(today.date())

# 3. Current Time
print("3. Current Time")
print(today.time())

# 4. Current Year
print("4. Current Year")
print(today.year)

# 5. Current Month
print("5. Current Month")
print(today.month)

# 6. Format Date

print("6. Format Date")
print(today.strftime("%d/%m/%y"))

# 7. Current Day
print("7. Current Day")
print(today.strftime("%A"))
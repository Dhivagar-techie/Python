# Write a Python program to display calendar

import calendar
Year=int(input("Enter the Year:"))
Month=int(input("Enter the month:"))
cal=calendar.month(Year,Month)
print(cal)
# Given your birthday and current date, calculate your age in days
# Compensate for leap days
# Assume that given birthday and current date are correct

def isLeapYear(y):
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        return True
    return False

def daysBetweenDates(d1, m1, y1, d2, m2, y2):
    daysInMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    years = (y2 - y1) * 365
    months = sum([daysInMonths[x - 1] for x in range(m1, m2 + 1)])
    days = d2 - d1

    leap = 0
    for y in range(y1, y2):
        if isLeapYear(y):
            leap += 1

    total = years + months + days + leap
    return total

print(daysBetweenDates(31, 8, 1998, 20, 3, 2021))

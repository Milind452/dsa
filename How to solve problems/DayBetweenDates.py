# Given your birthday and current date, calculate your age in days
# Compensate for leap days
# Assume that given birthday and current date are correct

# STEP 1: define nextDay method to return the next day assuming that each month has 30 days
# Step 2: define dayBetweenDates to get approximate answers with nextDay ana  helper function dateIsBefore which tells if a date 1 is before date 2 or not
# STEP 3: Write defensive code to check for incorect inputs
# STEP 4: Write daysInMonth function to be able to calculate nextDay properly assuming no leap year
# STEP 5: implement incorrect daysInMonth function in nextDay
# STEP 6: design isLeapYear to check for leap years
# STEP 7: implement isLeapYear in daysInMonth function to get accurate result
# STEP 8: run and test daysBetweenDates


# check if given year is leap year or not
def isLeapYear(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False

# calculate exact number of days in given month assuming no leap year
def daysInMonth(year, month):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isLeapYear(year) and month == 2:
        return 29
    return days[month - 1]


###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    if day >= daysInMonth(year, month):
        if month == 12:
            year += 1
            month = 1
            day = 1
        else:
            month += 1
            day = 1
    else:
        day += 1

    return year, month, day



# Helper function for daysBetweenDates to find out if first date is before second date or not

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2 or month1 < month2 or day1 < day2:
        return True
    return False



# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
# 
        
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""

    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    count = 0 
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        count+= 1
    
    return count

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    
    for (args, answer) in test_cases:
        try:
            result = daysBetweenDates(*args)
            if result == answer and answer != "AssertionError":
                print("Test case passed!")
            else:
                print("Test with data:", args, "failed")
    
        except AssertionError:
            if answer == "AssertionError":
                print("Nice job! Test case {0} correctly raises AssertionError!\n".format(args))
            else:
                print("Check your work! Test case {0} should not raise AssertionError!\n".format(args))    

test()

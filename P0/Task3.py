"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re
with open('P0/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('P0/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def isFixedLine(number):
  if number[0] == '(':
    return True
  return False

def getAreaCode(number):
  if not isFixedLine(number):
    # print("Not a fixed line number")
    return -1
  code = re.findall(r'\(.*?\)', number)
  return str(code)[3:-3]

def isBangalore(number):
  if getAreaCode(number) == '080':
    return True
  return False

def isMobile(number):
  mobilePrefix = ('7', '8', '9')
  if number[0] in mobilePrefix:
    return True
  return False
  
def getMobilePrefix(number):
  if not isMobile(number):
    # print("Not a mobile number")
    return -1
  return number[:4]

def isTelemarketer(number):
  if number[0] == '1':
    return True
  return False
  
def getTelemarketerCode(number):
  if not isTelemarketer(number):
    # print("Not a telemarketer number")
    return -1
  return number[:3]

codes = list()
for call in calls:
  if isBangalore(call[0]):
    number = call[1]
    code = ''
    if isFixedLine(number):
      code = getAreaCode(number)
    elif isMobile(number):
      code = getMobilePrefix(number)
    elif isTelemarketer(number):
      code = getTelemarketerCode
    
    if code not in codes:
      codes.append(code)


print("The numbers called by people in Bangalore have codes:")
for code in sorted(codes):
  print(code)

caller = len(codes)
receiver = 0
for code in codes:
  if code == '080':
    receiver += 1

print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore".format(receiver / caller * 100))
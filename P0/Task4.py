"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('P0/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('P0/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def isTelemarketer(number):
  if number[0] == '1':
    return True
  return False

callSend = list()
callReceive = list()
textSend = list()
textReceive = list()
for call, text in zip(calls, texts):
    callReceive.append(call[1])
    textReceive.append(text[1])
    textSend.append(text[0])

for call in calls:
    number = call[0]
    if isTelemarketer(number) and number not in callReceive and number not in textReceive and number not in textSend:
        callSend.append(number)

print("These numbers could be telemarketers:")
for number in sorted(callSend):
    print(number)


# Worst case Big O Notation: O(2)
"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('P0/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('P0/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
m = -1
mNumber = ''
for call in calls:
    number = call[0]
    duration = int(call[3])
    if duration > m:
        m = duration
        mNumber = number

print("{} spent the longest time, {} seconds, on the phone during September 2016".format(mNumber, m))


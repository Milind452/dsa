"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from collections import Counter
with open('P0/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('P0/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
record = dict()
for text, call in zip(texts, calls):
    if text[0] not in record:
        record[text[0]] = 1
    else:
        record[text[0]] += 1
    if text[1] not in record:
        record[text[1]] = 1
    else:
        record[text[1]] += 1
    if call[0] not in record:
        record[call[0]] = 1
    else:
        record[call[0]] += 1
    if call[1] not in record:
        record[call[1]] = 1
    else:
        record[call[1]] += 1

print("There are {} different telephone numbers in the records".format(len(record)))


# Worst case Big O Notation: O(n)
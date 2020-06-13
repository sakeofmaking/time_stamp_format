"""
Time Stamp Format

Description: Take time stamp of format #h#m#s#ms and reformat as ##:##:##:###

Author: Nic La
Last modified: Jun 2020
"""


import csv
import re


# Initialize variables
original_file = 'example_short.txt'
new_file = 'example_new.txt'
raw = []
clean_time = []
pattern_h = r'(\d{1,3})h'
pattern_m = r'(\d{1,3})m(?!s)'
pattern_s = r'(\d{1,3})s'
pattern_ms = r'(\d{1,3})ms'


# Open csv file
# file separated via ';'
# row 1 - 19 contain irrelevant data
# row 20 contains header
# row 21 contains no data
# first column contains timestamp
# load csv file contents into list (may exceed RAM limits)
with open(original_file) as in_file:
    reader = csv.reader(in_file, delimiter=';')
    for row in reader:
        raw.append(row)


# Use regex to replace h, m, s, ms in column 1 data
for line in raw[21:]:
    match_h = re.search(pattern_h, line[0])
    match_m = re.search(pattern_m, line[0])
    match_s = re.search(pattern_s, line[0])
    match_ms = re.search(pattern_ms, line[0])
    if match_h is None:
        h = 0
    else:
        h = match_h[1]
    if match_m is None:
        m = 0
    else:
        m = match_m[1]
    if match_s is None:
        s = 0
    else:
        s = match_s[1]
    if match_ms is None:
        ms = 0
    else:
        ms = match_ms[1]
    line[0] = str(h) + ':' + str(m) + ':' + str(s) + ':' + str(ms)


# Return all data to new csv file
with open(new_file, 'w') as out_file:
    writer = csv.writer(out_file, delimiter=';')
    writer.writerows(raw)

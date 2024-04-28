#!/usr/bin/env python3
"""reducer.py"""

from operator import itemgetter
import sys

current_score = None
current_sum = 0
current_count = 0

for line in sys.stdin:
    score, count = line.strip().split("\t", 2)
    
    try:
        count = int(count)
    except ValueError:
        continue
    
    if current_score == score:
        current_sum += count
        current_count += 1
    else:
        if current_score:
            average = current_sum / current_count
            print(f"{current_score}\t{average}")
        current_score = score
        current_sum = count
        current_count = 1

if current_score:
    average = current_sum / current_count
    print(f"{current_score}\t{average}")

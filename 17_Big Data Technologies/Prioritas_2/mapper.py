#!/usr/bin/env python3
"""mapper.py"""

import sys

for line in sys.stdin:
    scores = line.strip().split()
    
    for score in scores:
        print(f"score\t{score}\t{1}")
